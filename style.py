import streamlit as st

def load_css():
    """
    Fungsi untuk memuat CSS kustom untuk styling.
    """
    st.markdown("""
    <style>
        /* Sembunyikan sidebar bawaan Streamlit */
        [data-testid="stSidebar"] {
            display: none;
        }
                
        /* Mengatur jarak antar kolom grid */
        .st-emotion-cache-1r6slb0 {
            gap: 3rem;
        }
                
        /* CSS untuk kotak biru bernomor */
        .step-number {
            background-color: #0d6efd;
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            padding: 1.5rem;
            border-radius: 10px;
            display: inline-block;
            width: 80px;
            height: 80px;
            text-align: center;
            line-height: 2.5rem;
            margin-bottom: 1rem;
        }
                
        /* Menghilangkan padding atas bawaan streamlit */
        .st-emotion-cache-18ni7ap {
            padding-top: 2rem;
        }
        .st-emotion-cache-z5fcl4 {
            padding-top: 3rem;
        }

        /* Tombol Primary (Sign Up & Get Started) */
        .stButton > button.primary {
            background-color: #0d6efd;
            border-color: #0d6efd;
            color: white;
        }
        .stButton > button.primary:hover {
            background-color: #0b5ed7;
            border-color: #0b5ed7;
        }

        /* Tombol Secondary (Login) */
        .stButton > button:not(.primary) {
            background-color: transparent;
            border: 1px solid #0d6efd;
            color: #0d6efd;
        }
        .stButton > button:not(.primary):hover {
            background-color: #0d6efd;
            color: white;
        }
                
        /* --- Extract.py --- */
        .stFileUploader button {
            background-color: #0d6efd;
            color: white;
            border: 1px solid #0d6efd;
        }
        .stFileUploader button:hover {
            background-color: #0b5ed7;
            border: 1px solid #0b5ed7;
            color: white;
        }
        .stFileUploader label {
            font-size: 1.1rem !important;
            font-weight: 500;
            color: #555;
        }

        /* --- TAMBAHAN BARU: Style untuk Header Logo --- */
        .header-logo {
            color: #0d6efd !important;
            margin: 0;
            padding-top: 15px; /* Mengatur posisi agar sejajar menu */
            font-weight: 700; /* Bold */
            font-size: 2rem; /* Ukuran h2 standar */
        }

        /* --- TAMBAHAN BARU: ABOUT US PAGE --- */
        
        /* Judul Halaman */
        .team-title {
            color: #0d6efd; /* Biru Strukify */
            text-align: center;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }

        /* Container Kartu */
        .team-card {
            background-color: #e0e0e0; /* Abu-abu seperti di desain */
            padding: 2rem 1rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Bayangan halus */
            height: 100%;
            transition: transform 0.2s; /* Efek saat hover */
            color: #333;
        }
        
        .team-card:hover {
            transform: translateY(-5px); /* Kartu naik sedikit saat di-hover */
        }

        /* Ikon Orang (Lingkaran) */
        .icon-box {
            width: 80px;
            height: 80px;
            border: 4px solid #333;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem auto;
        }
        
        /* Nama Anggota */
        .member-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #000;
        }

        /* Deskripsi Lorem Ipsum */
        .member-desc {
            font-size: 0.8rem;
            color: #555;
            margin-bottom: 1.5rem;
            line-height: 1.4;
        }

        /* Nomor ID (NIM) */
        .member-id {
            font-size: 0.9rem;
            font-weight: 800;
            color: #000;
        }
                
        /* --- TAMBAHAN BARU: ABOUT US PAGE (DARK MODE) --- */
        
        /* Judul Halaman (Biru) */
        .team-title {
            color: #0d6efd !important; /* Warna Biru */
            text-align: center;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }

        /* Container Kartu (Abu Gelap) */
        .team-card {
            background-color: #262730; /* Abu gelap (khas komponen dark mode) */
            padding: 2rem 1rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3); /* Bayangan sedikit lebih gelap */
            height: 100%;
            transition: transform 0.2s;
            border: 1px solid #444; /* Border tipis agar lebih tegas */
        }
        
        .team-card:hover {
            transform: translateY(-5px);
            border-color: #0d6efd; /* Efek border biru saat di-hover */
        }

        /* Ikon Orang (Lingkaran Putih) */
        .icon-box {
            width: 80px;
            height: 80px;
            border: 3px solid white; /* Garis lingkaran putih */
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem auto;
            color: white; /* Warna ikon di dalamnya putih */
        }
        
        /* Nama Anggota (Putih) */
        .member-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: white; /* Text Putih */
        }

        /* Deskripsi (Abu Terang) */
        .member-desc {
            font-size: 0.8rem;
            color: #cccccc; /* Abu terang agar enak dibaca di background gelap */
            margin-bottom: 1.5rem;
            line-height: 1.4;
        }

        /* Nomor ID (Putih Tebal) */
        .member-id {
            font-size: 0.9rem;
            font-weight: 800;
            color: white; /* Text Putih */
            opacity: 0.8;
        }
                
    </style>
    """, unsafe_allow_html=True)