import streamlit as st
from PIL import Image
import time
from style import load_css     # Impor dari root direktori
from header import render_header # Impor dari root direktori

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Extract Receipt",
    page_icon="🧾",
    layout="wide"
)

# --- 1. MEMUAT ASET (CSS & HEADER) ---
load_css()
render_header()

# --- 2. JUDUL KONTEN ---
# Menggunakan markdown untuk membuat semua teks rata tengah
st.markdown("<h1 style='text-align: center;'>Upload receipt here</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Transform your receipts into smart and structured data instantly!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>No manual typing. No hassle. Just upload and extract.</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- 3. UPLOADER (CENTERED) ---
# Kita gunakan kolom untuk memusatkan file uploader
col1, col_main, col3 = st.columns([1, 1.5, 1])

with col_main:
    # Label uploader akan menjadi teks "Or drag & drop files here"
    # Tombol "Browse files" akan otomatis menjadi biru karena CSS
    uploaded_file = st.file_uploader(
        "Or drag & drop files here", 
        type=["jpg", "jpeg", "png", "pneg"], # Menambahkan PNEG
        label_visibility="visible" # Tampilkan label "Or drag & drop..."
    )
    
    # Menambahkan teks kecil di bawahnya
    st.markdown("<p style='text-align: center; color: #888; margin-top: -10px;'>Only JPG, PNG & PNEG files!</p>", unsafe_allow_html=True)


# --- 4. LOGIKA SETELAH UPLOAD ---
# Ini akan ditampilkan SETELAH file di-upload
if uploaded_file is not None:
    
    # Kita tampilkan gambar dan tombol di dalam kolom yang sama
    with col_main:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_column_width=True)
        
        st.divider()
        
        # Tombol untuk memulai proses ekstraksi
        if st.button("✨ Extract Data", type="primary", use_container_width=True):
            
            with st.spinner('Scanning receipt... Our AI is working its magic!'):
                # --- (DI SINI ANDA MEMANGGIL MODEL CV ANDA) ---
                time.sleep(3) # Hapus ini, ini hanya simulasi
                
                # --- Tampilkan Hasil (Contoh) ---
                st.success('Extraction Complete!')
                
                st.subheader("Extracted Information")
                st.write("Please review the data. You can edit it before saving.")
                
                st.text_input("Store Name", value="Contoh Mart")
                st.date_input("Date", value=None) 
                st.text_input("Total Amount", value="Rp 50.000")
                
                st.subheader("Items")
                st.text_area("Items List", 
                             value="- Item 1: Rp 20.000\n- Item 2: Rp 30.000", 
                             height=150)
                
                if st.button("Save to History"):
                    st.toast("Data saved!", icon="✅")