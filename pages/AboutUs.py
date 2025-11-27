import streamlit as st
from style import load_css
from header import render_header

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="About Us",
    page_icon="🧾",
    layout="wide"
)

# --- MEMUAT ASET & NAVIGASI ---
load_css()
render_header(current_page_index=3)

# --- JUDUL ---
st.markdown('<h1 class="team-title">Meet Our Team</h1>', unsafe_allow_html=True)

# --- DATA TIM ---
# Kita buat list dictionary agar kodenya rapi dan mudah diedit
team_members = [
    {
        "name": "Bryan",
        "id": "412023005",
        "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore."
    },
    {
        "name": "Kink Kusto",
        "id": "412023006",
        "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore."
    },
    {
        "name": "Nelson",
        "id": "412023008",
        "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore."
    },
    {
        "name": "Gaudensius",
        "id": "412023018",
        "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore."
    }
]

# --- LAYOUT GRID (4 Kolom) ---
cols = st.columns(4)

# Loop untuk mengisi setiap kolom dengan kartu anggota
# --- LAYOUT GRID (4 Kolom) ---
cols = st.columns(4)

# Loop untuk mengisi setiap kolom dengan kartu anggota
for i, member in enumerate(team_members):
    with cols[i]:
        # PERBAIKAN: HTML diratakan ke kiri (tanpa spasi di awal) 
        # agar tidak dianggap sebagai code block
        st.markdown(f"""
<div class="team-card">
    <div class="icon-box">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
        </svg>
    </div>
    <div class="member-name">{member['name']}</div>
    <div class="member-desc">{member['desc']}</div>
    <div class="member-id">{member['id']}</div>
</div>
""", unsafe_allow_html=True)
        
st.write("<br><br>", unsafe_allow_html=True)