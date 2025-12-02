import streamlit as st
import pandas as pd
import os
from style import load_css
from header import render_header

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="History", page_icon="🧾", layout="wide")
load_css()
render_header(current_page_index=2)

# --- LOAD DATA CSV ---
CSV_PATH = "history_data.csv"
data_history = []

if os.path.exists(CSV_PATH):
    try:
        df = pd.read_csv(CSV_PATH)
        # Konversi ke list of dict agar mudah di-loop sesuai kode UI lama
        data_history = df.to_dict('records')
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
else:
    # Jika file belum ada, biarkan kosong
    data_history = []


# --- UI HEADER ---
st.title("History")

col1, col2, col3 = st.columns([2, 1, 1.2]) 
with col1:
    search_term = st.text_input("Search", placeholder="Search store...", label_visibility="collapsed")
with col2:
    st.selectbox("Filter dates", ["All dates", "Today"], label_visibility="collapsed")
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

# --- MENAMPILKAN DATA ---
if not data_history:
    st.info("Belum ada riwayat. Silakan extract data terlebih dahulu.")
else:
    # Reverse agar data terbaru muncul paling atas
    for i, item in enumerate(reversed(data_history)):
        
        # Filter Search Sederhana
        if search_term and search_term.lower() not in str(item['store']).lower():
            continue

        with st.container(border=True):
            col_r1, col_r2, col_r3, col_r4, col_r5 = st.columns([0.5, 3, 2, 2, 1])
            
            with col_r1:
                st.write(f"{len(data_history) - i}") # Nomor urut
            
            with col_r2:
                st.write(f"<span style='font-size: 1.1em;'>{item['store']}</span>", unsafe_allow_html=True)
            
            with col_r3:
                st.write(str(item['date']))
            
            with col_r4:
                # Format Rupiah Sederhana
                try:
                    amount = float(str(item['total']).replace('Rp','').replace('.','').replace(',',''))
                    fmt_money = f"Rp {amount:,.0f}".replace(",", ".")
                except:
                    fmt_money = str(item['total'])
                st.write(fmt_money)
            
            with col_r5:
                st.button("👁️", key=f"view_{i}")

    st.write("")

st.divider()

# --- FOOTER SUMMARY ---
col_f1, col_f2 = st.columns(2)
total_receipts = len(data_history)
with col_f1:
    st.markdown(f"**{total_receipts} receipts**")