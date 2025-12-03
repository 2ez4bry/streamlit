import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import cv2
import easyocr
import pandas as pd
from datetime import date
import os
import re  # <--- ADD THIS LINE
import tensorflow as tf
import keras_cv 
from tensorflow.keras.models import load_model
from style import load_css
from header import render_header

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Extract", page_icon="🧾", layout="wide")
load_css()
render_header(current_page_index=1)

# --- KONFIGURASI MODEL & DATA ---
# Sesuaikan nama file dengan yang ada di folder project
MODEL_PATH = "best_retinanet_yahaha-elikpaddle.keras" 
CSV_PATH = "history_data.csv"
# Input size RetinaNet biasanya harus kelipatan 64 atau sesuai training config (misal 640x640)
# Jika di Colab Anda resize ke 640, ubah disini jadi (640, 640)
TARGET_SIZE = (640, 640) 

# --- 1. SETUP & CACHING RESOURCE (BACKEND) ---
@st.cache_resource
def load_resources():
    # Load Model RetinaNet
    # Pastikan file .keras ada di folder utama (satu level di atas folder pages/)
    # Jika file ada di root, gunakan '../best_retinanet...' atau path absolut
    model_path = 'best_retinanet_yahaha-elikpaddle.keras' 
    
    try:
        model = tf.keras.models.load_model(model_path, compile=False)
        # Load EasyOCR (CPU Mode biar aman di Streamlit)
        reader = easyocr.Reader(['id', 'en'], gpu=False)
        return model, reader
    except Exception as e:
        return None, None

# --- 2. LOGIKA PARSING V6 (GACOR) ---
def parse_receipt_v6(text_list):
    final_data = {"store": None, "date": None, "total": 0, "items": []}
    
    BANNED_WORDS = [
        "CASHIER", "KASIR", "POS", "TAX", "PPN", "CHANGE", "KEMBALI", 
        "TUNAI", "CASH", "CARD", "DEBIT", "TELP", "JL.", "JAKARTA", 
        "TERIMA", "THANK", "SALES", "RECEIPT", "RCT", "ID", "MEMBER",
        "SC", "PB1", "SUBTOTAL", "TOTAL", "AMOUNT", "PAYMENT"
    ]

    clean_lines = [line.strip() for line in text_list if line.strip()]
    parsed_items = []
    
    # Metadata
    if clean_lines: final_data['store'] = clean_lines[0]
    for line in clean_lines:
        match = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{4})', line)
        if match: final_data['date'] = match.group(0); break

    used_indices = set()

    def is_calculation_line(text):
        norm = text.replace('o','0').replace('O','0').replace('l','1').upper()
        if re.search(r'\d\s*[X]', norm) or re.search(r'[X]\s*\d', norm) or "X /" in norm: return True 
        return False

    def is_garbage(text):
        if len(text) < 3: return True
        if re.match(r'^[\d\W_]+$', text): return True
        return False

    for i, line in enumerate(clean_lines):
        line_upper = line.upper()
        
        # 1. Diskon
        discount_match = re.search(r'^[~-]\s*(\d{1,3}[.,]\d{3})', line.replace('o','0'))
        if discount_match:
            val_str = discount_match.group(1)
            val = int(re.sub(r'[^\d]', '', val_str))
            parsed_items.append({"name": "DISKON / POTONGAN", "price": -val, "qty": 1})
            used_indices.add(i); continue

        # 2. Harga Normal
        line_fix = line.replace('o','0').replace('O','0').replace('l','1')
        price_match = re.search(r'(\d{1,3}\s*[.,]\s*\d{3})\s*$', line_fix)
        
        if price_match:
            price_str = price_match.group(1)
            price_val = int(re.sub(r'[^\d]', '', price_str))
            
            if 500 <= price_val <= 10000000:
                found_name = None
                for k in range(1, 5): 
                    idx = i - k
                    if idx < 0: break
                    if idx in used_indices: continue 
                    candidate = clean_lines[idx]
                    cand_upper = candidate.upper()
                    
                    if is_calculation_line(candidate): continue
                    if is_garbage(candidate): continue        
                    if re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{4}', candidate): continue
                    if re.search(r'\d{10,}', candidate): continue
                    if any(b in cand_upper for b in BANNED_WORDS): continue
                    
                    found_name = candidate
                    used_indices.add(idx)
                    used_indices.add(i)
                    break 
                
                if found_name and not any(x['name'] == found_name for x in parsed_items):
                    parsed_items.append({"name": found_name, "price": price_val, "qty": 1})

    if parsed_items:
        final_data['total'] = sum(x['price'] for x in parsed_items)
        final_data['items'] = parsed_items
    
    return final_data

# --- 3. FUNGSI PROCESS IMAGE (RETINANET + OCR) ---
def process_receipt_image(uploaded_file, model, reader):
    # Convert Streamlit file to OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    h, w, _ = img.shape
    
    # Deteksi RetinaNet
    img_resized = cv2.resize(img, (640, 640))
    input_tensor = np.expand_dims(img_resized, axis=0)
    
    detections = model.predict(input_tensor, verbose=0)
    
    if isinstance(detections, dict):
        boxes, scores = detections['boxes'][0], detections['confidence'][0]
    else:
        boxes, scores = detections[0][0], detections[1][0]

    best_idx = np.argmax(scores)
    
    # Crop Logic
    if scores[best_idx] < 0.2:
        roi = img # Fallback full image
    else:
        best_box = boxes[best_idx]
        if np.max(best_box) <= 1.0:
            y1, x1, y2, x2 = int(best_box[0]*h), int(best_box[1]*w), int(best_box[2]*h), int(best_box[3]*w)
        else:
            y1, x1, y2, x2 = int(best_box[0]), int(best_box[1]), int(best_box[2]), int(best_box[3])
        
        # --- PERBAIKAN DI SINI ---
        # Pastikan koordinat ada di dalam batas gambar
        y1, x1 = max(0, y1), max(0, x1)
        y2, x2 = min(h, y2), min(w, x2)

        # Cek apakah area crop valid (tidak 0 atau negatif)
        if y2 > y1 and x2 > x1:
            roi = img[y1:y2, x1:x2]
        else:
            # Jika box invalid, gunakan gambar full
            roi = img 

    # Zoom & OCR
    # Sekarang aman karena roi dijamin tidak kosong
    roi_enhanced = cv2.resize(roi, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    raw_text = reader.readtext(roi_enhanced, detail=0)  
    
    return roi, raw_text

# --- LOAD MODEL ---
model, reader = load_resources()

if model is None:
    st.error("⚠️ Model AI tidak ditemukan! Pastikan file 'best_retinanet...keras' ada di folder utama.")
    st.stop()

# --- JUDUL KONTEN ---
st.markdown("<h1 style='text-align: center;'>Upload receipt here</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Transform your receipts into smart and structured data instantly!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>No manual typing. No hassle. Just upload and extract.</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- UPLOADER (CENTERED) ---
col1, col_main, col3 = st.columns([1, 1.5, 1])

with col_main:
    uploaded_file = st.file_uploader(
        "Or drag & drop files here", 
        type=["jpg", "jpeg", "png", "pneg"], 
        label_visibility="visible"
    )
    st.markdown("<p style='text-align: center; color: #888; margin-top: -10px;'>Only JPG, PNG files!</p>", unsafe_allow_html=True)

# --- LOGIKA SETELAH UPLOAD ---
if uploaded_file is not None:
    with col_main:
        # Tampilkan gambar yang diupload
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_container_width=True)
        
        st.divider()
        
        # Tombol Ekstraksi
        if st.button("✨ Extract Data", type="primary", use_container_width=True):
            
            with st.spinner('Scanning receipt... Our AI is working its magic!'):
                try:
                    # Reset pointer file agar bisa dibaca opencv
                    uploaded_file.seek(0)
                    
                    # 1. Proses Gambar (Crop & OCR)
                    roi_img, text_ocr = process_receipt_image(uploaded_file, model, reader)
                    
                    # 2. Parsing Data (Logic V6)
                    result_data = parse_receipt_v6(text_ocr)
                    
                    # Simpan ke session state agar tidak hilang saat input diedit
                    st.session_state['extracted_data'] = result_data
                    st.session_state['cropped_image'] = roi_img
                    
                    st.toast("Extraction Complete!", icon="✅")
                    
                except Exception as e:
                    st.error(f"Error during extraction: {e}")

# --- TAMPILKAN HASIL EKSTRAKSI ---
if 'extracted_data' in st.session_state:
    data = st.session_state['extracted_data']
    
    # Layout Kolom untuk Hasil
    with col_main:
        st.success('Extraction Complete!')
        
        # Tampilkan Hasil Crop (Opsional, biar keren)
        with st.expander("View Auto-Cropped Receipt"):
            st.image(st.session_state['cropped_image'], channels="BGR", use_container_width=True)

        st.subheader("Extracted Information")
        st.write("Please review the data. You can edit it before saving.")
        
        # Form Input Terisi Otomatis
        store_name = st.text_input("Store Name", value=data['store'] if data['store'] else "Unknown Store")
        date_val = st.text_input("Date", value=data['date'] if data['date'] else "") 
        total_val = st.text_input("Total Amount", value=f"{data['total']:,}")
        
        st.subheader("Items")
        
        # Tampilkan item dalam bentuk Tabel yang bisa diedit (Data Editor)
        if data['items']:
            df_items = pd.DataFrame(data['items'])
            edited_df = st.data_editor(
                df_items, 
                column_config={
                    "name": "Item Name",
                    "price": st.column_config.NumberColumn("Price (Rp)", format="%d"),
                    "qty": "Qty"
                },
                use_container_width=True,
                num_rows="dynamic" # User bisa tambah baris manual
            )
        else:
            st.warning("No items detected automatically. You can add them manually.")
            # Tabel kosong untuk input manual
            empty_df = pd.DataFrame(columns=["name", "price", "qty"])
            edited_df = st.data_editor(empty_df, num_rows="dynamic", use_container_width=True)

        st.write("<br>", unsafe_allow_html=True)
        
        # --- PERBAIKAN LOGIKA SAVE ---
        if st.button("Save to History", use_container_width=True):
            # 1. AMBIL DATA DARI HASIL EDIT (Bukan hasil scan awal)
            
            # A. Ambil Item dari Tabel Editor
            # edited_df adalah variabel hasil dari st.data_editor di atas
            if edited_df is not None:
                final_items = edited_df.to_dict('records')
            else:
                final_items = []
            
            # B. Bersihkan Total (Hapus titik/koma agar jadi angka murni)
            # Contoh input: "100.000" -> jadi integer 100000
            try:
                clean_total_str = str(total_val).replace(',', '').replace('.', '')
                clean_total = int(clean_total_str)
            except:
                clean_total = 0

            # 2. Siapkan Record Baru
            new_record = {
                "id": int(pd.Timestamp.now().timestamp()), 
                "store": store_name,     # <--- Pakai variabel input text
                "date": date_val,        # <--- Pakai variabel input text
                "total": clean_total,    # <--- Pakai total yang sudah dibersihkan
                "items": str(final_items) # Simpan list sebagai string agar masuk CSV
            }
            
            # 3. Simpan ke CSV
            history_file = "history_data.csv"
            df_new = pd.DataFrame([new_record])
            
            if not os.path.exists(history_file):
                df_new.to_csv(history_file, index=False)
            else:
                df_new.to_csv(history_file, mode='a', header=False, index=False)
            
            st.toast("Data saved successfully with YOUR EDITS!", icon="✅")
            st.balloons()