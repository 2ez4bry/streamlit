import streamlit as st
import pandas as pd
import os
import ast
from datetime import datetime # <--- Tambahan import untuk waktu
from style import load_css
from header import render_header

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="History", page_icon="🧾", layout="wide")
load_css()
render_header(current_page_index=2)

# --- FUNGSI POP-UP DETAIL (DIALOG) ---
@st.dialog("Rincian Transaksi")
def show_details(item):
    st.write(f"**Toko:** {item.get('store', '-')}")
    st.write(f"**Tanggal:** {item.get('date', '-')}")
    
    # Parsing Data Items dari String ke List
    raw_items = item.get('items', '[]')
    try:
        list_items = ast.literal_eval(raw_items)
        
        if isinstance(list_items, list) and len(list_items) > 0:
            df_items = pd.DataFrame(list_items)
            st.dataframe(
                df_items,
                column_config={
                    "name": "Nama Barang",
                    "price": st.column_config.NumberColumn("Harga", format="Rp %d"),
                    "qty": st.column_config.NumberColumn("Jml", format="%d")
                },
                use_container_width=True,
                hide_index=True
            )
            
            total_check = sum(x['price'] for x in list_items)
            st.write(f"**Total Kalkulasi:** Rp {total_check:,}")
        else:
            st.warning("Data item kosong atau tidak terbaca.")
            
    except Exception as e:
        st.error(f"Gagal memproses detail item: {e}")

# --- LOAD DATA CSV ---
CSV_PATH = "history_data.csv"
data_history = []

if os.path.exists(CSV_PATH):
    try:
        df = pd.read_csv(CSV_PATH)
        data_history = df.to_dict('records')
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
else:
    data_history = []

# --- UI HEADER ---
st.title("History")

col1, col2, col3 = st.columns([2, 1, 1.2]) 
with col1:
    search_term = st.text_input("Search", placeholder="Search store...", label_visibility="collapsed")

with col2:
    # 1. Simpan pilihan user ke variabel 'filter_date'
    filter_date = st.selectbox("Filter dates", ["All dates", "Today"], label_visibility="collapsed")

with col3:
    if st.button("Upload new receipt", type="primary", use_container_width=True):
        st.switch_page("pages/Extract.py")

st.divider()

# --- TABEL CUSTOM ---
col_h1, col_h2, col_h3, col_h4, col_h5 = st.columns([0.5, 3, 2, 2, 1])
with col_h1: st.write("**#**") 
with col_h2: st.write("**Store Name**")
with col_h3: st.write("**Date**")
with col_h4: st.write("**Total**")
with col_h5: st.write("**View**")

# --- MENAMPILKAN DATA (DENGAN FILTER) ---
if not data_history:
    st.info("Belum ada riwayat. Silakan extract data terlebih dahulu.")
else:
    # Counter untuk nomor urut tampilan
    display_count = 0
    
    # Reverse agar data terbaru muncul paling atas
    for i, item in enumerate(reversed(data_history)):
        
        # --- LOGIKA FILTER SEARCH ---
        store_name = str(item.get('store', '')).lower()
        if search_term and search_term.lower() not in store_name:
            continue

        # --- LOGIKA FILTER TANGGAL (BARU) ---
        if filter_date == "Today":
            try:
                # Ambil tanggal dari item (misal: "25/12/2023" atau "5-12-2023")
                date_str = str(item.get('date', ''))
                
                # Gunakan pandas to_datetime agar pintar membaca format dd/mm/yyyy
                # dayfirst=True penting agar 01/02 dibaca 1 Feb, bukan 2 Jan
                item_date = pd.to_datetime(date_str, dayfirst=True).date()
                today_date = pd.Timestamp.now().date()
                
                # Jika tanggal tidak sama dengan hari ini, lewati (skip)
                if item_date != today_date:
                    continue
            except:
                # Jika format tanggal error/kosong, skip saja agar aman
                continue

        # Jika lolos semua filter, tampilkan baris
        display_count += 1
        
        with st.container(border=True):
            col_r1, col_r2, col_r3, col_r4, col_r5 = st.columns([0.5, 3, 2, 2, 1])
            
            with col_r1:
                st.write(f"{display_count}") # Nomor urut dinamis
            
            with col_r2:
                st.write(f"<span style='font-size: 1.1em;'>{item.get('store', '-')}</span>", unsafe_allow_html=True)
            
            with col_r3:
                st.write(str(item.get('date', '-')))
            
            with col_r4:
                try:
                    val_str = str(item.get('total', 0))
                    amount = float(val_str.replace('Rp','').replace('.','').replace(',',''))
                    fmt_money = f"Rp {amount:,.0f}".replace(",", ".")
                except:
                    fmt_money = str(item.get('total', '-'))
                st.write(fmt_money)
            
            with col_r5:
                # Tombol View dengan Dialog
                if st.button("👁️", key=f"view_{item.get('id', i)}"): # Pakai ID unik jika ada agar key aman
                    show_details(item)

    # Pesan jika hasil filter kosong
    if display_count == 0:
        st.warning("Tidak ditemukan transaksi yang sesuai filter.")

    st.write("")

st.divider()

# --- FOOTER SUMMARY ---
col_f1, col_f2 = st.columns(2)
# Tampilkan jumlah yang sedang dilihat vs total
with col_f1:
    st.markdown(f"**Showing {display_count} of {len(data_history)} receipts**")