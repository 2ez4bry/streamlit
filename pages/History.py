import streamlit as st
import datetime
from style import load_css     # Impor dari root direktori
from header import render_header # Impor dari root direktori

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="History",
    page_icon="🧾",
    layout="wide"
)

# --- 1. MEMUAT ASET & NAVIGASI ---
load_css()

# "History" adalah item ke-3 di menu, jadi index-nya 2
render_header(current_page_index=2) 

# --- LOGIKA PINDAH HALAMAN ---
#if selected == "Home":
#    st.switch_page("streamlit_app.py")
#if selected == "Extract":
#    st.switch_page("pages/Extract.py")
#if selected == "Analysis":
#    st.switch_page("pages/Analysis.py")

# --- (DATA) ---
# Data dikosongkan sesuai permintaan. 
# Nantinya, Anda akan mengambil data ini dari database.
mock_data = []

# --- 2. JUDUL & KONTROL ---
st.title("History")

col1, col2, col3 = st.columns([2, 1, 1.2]) 
with col1:
    st.text_input(
        "Search", 
        placeholder="Search by store name...", 
        label_visibility="collapsed"
    )
with col2:
    st.selectbox(
        "Filter dates", 
        ["All dates", "Today", "Last 7 days", "This month"], 
        label_visibility="collapsed"
    )
with col3:
    # Tombol ini sekarang akan pindah ke halaman Extract saat diklik
    if st.button("Upload new receipt", type="primary", use_container_width=True):
        st.switch_page("pages/Extract.py")

st.divider()

# --- 3. DAFTAR HISTORY (HEADER) ---
col_h1, col_h2, col_h3, col_h4, col_h5 = st.columns([0.5, 3, 2, 2, 1])
with col_h1:
    st.write("**Receipt**") 
with col_h2:
    st.write("**Store Name**")
with col_h3:
    st.write("**Date**")
with col_h4:
    st.write("**Total**")
with col_h5:
    st.write("**View**")

# --- 4. DAFTAR HISTORY (ISI) ---
# Cek apakah ada data. Jika tidak, tampilkan pesan.
if not mock_data:
    st.info("Belum ada riwayat ekstraksi. Silakan upload struk baru.")
else:
    # Jika ada data, loop dan tampilkan
    for item in mock_data:
        with st.container(border=True):
            col_r1, col_r2, col_r3, col_r4, col_r5 = st.columns([0.5, 3, 2, 2, 1])
            
            with col_r1:
                st.checkbox(f"select_{item['id']}", label_visibility="collapsed", key=f"check_{item['id']}")
            
            with col_r2:
                st.write(f"<span style='font-size: 1.1em;'>{item['store']}</span>", unsafe_allow_html=True)
            
            with col_r3:
                st.write(item['date'].strftime("%d %b, %Y"))
            
            with col_r4:
                total_formatted = f"Rp.{item['total']:,}".replace(",", ".") + ",00"
                st.write(total_formatted)
            
            with col_r5:
                if st.button("👁️", key=f"view_{item['id']}", use_container_width=True):
                    st.toast(f"Viewing receipt from {item['store']}...") 
    
    st.write("") # Memberi spasi antar baris

st.divider()

# --- 5. FOOTER SUMMARY ---
col_f1, col_f2 = st.columns(2)

total_receipts = len(mock_data)
total_amount = sum(item['total'] for item in mock_data)
total_amount_formatted = f"Rp.{total_amount:,}".replace(",", ".") + ",00"

with col_f1:
    st.markdown(f"**{total_receipts} receipts**")
with col_f2:
    st.markdown(f"**Total {total_amount_formatted}**")