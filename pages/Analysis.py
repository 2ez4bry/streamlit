import streamlit as st
import datetime
from style import load_css     # Impor dari root direktori
from header import render_header # Impor dari root direktori

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Analysis",
    page_icon="🧾",
    layout="wide"
)

# --- 1. MEMUAT ASET & NAVIGASI ---
load_css()

# "Analysis" adalah item ke-4 di menu, jadi index-nya 3
selected = render_header(default_index=3) 

# --- LOGIKA PINDAH HALAMAN ---
if selected == "Home":
    st.switch_page("streamlit_app.py")
if selected == "Extract":
    st.switch_page("pages/Extract.py")
if selected == "History":
    st.switch_page("pages/History.py")

# --- (DATA KOSONG) ---
# Data dikosongkan sesuai permintaan.
mock_data = []

# --- 2. JUDUL ---
st.title("Analysis")

# --- 3. KALKULASI METRIK ---
total_receipts = len(mock_data)

if total_receipts > 0:
    total_spending = sum(item['total'] for item in mock_data)
    average_spending = total_spending / total_receipts
    
    total_spending_formatted = f"Rp.{total_spending:,.0f}".replace(",", ".") + ",00"
    
    avg_int = int(average_spending)
    avg_dec = int((average_spending - avg_int) * 100)
    average_spending_formatted = f"Rp.{avg_int:,},{avg_dec}"

else:
    # Jika tidak ada data, semua diatur ke 0
    total_receipts = 0
    total_spending_formatted = "Rp.0,00"
    average_spending_formatted = "Rp.0,00"

st.write("") # Memberi spasi

# --- 4. MENAMPILKAN METRIK ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Receipts", 
        value=total_receipts # Akan menampilkan 0
    )
    
with col2:
    st.metric(
        label="Average", 
        value=average_spending_formatted # Akan menampilkan Rp.0,00
    )

with col3:
    st.metric(
        label="Total spending", 
        value=total_spending_formatted # Akan menampilkan Rp.0,00
    )

st.divider()

# Area chart
st.subheader("Spending Charts")
st.info("Tidak ada data untuk ditampilkan di chart. Silakan upload struk terlebih dahulu.")