import streamlit as st

def load_css():
    """
    Fungsi untuk memuat CSS kustom untuk styling.
    """
    st.markdown("""
    <style>
        /* Mengatur jarak antar kolom grid */
        .st-emotion-cache-1r6slb0 {
            gap: 3rem;
        }
                
        /* CSS untuk kotak biru bernomor */
        .step-number {
            background-color: #0d6efd; /* Warna biru (mirip prototipe) */
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            padding: 1.5rem;
            border-radius: 10px;
            display: inline-block;
            width: 80px;
            height: 80px;
            text-align: center;
            line-height: 2.5rem; /* Menyesuaikan agar angka ditengah */
            margin-bottom: 1rem;
        }
                
        /* Menghilangkan padding atas bawaan streamlit */
        .st-emotion-cache-18ni7ap {
            padding-top: 2rem;
        }
        .st-emotion-cache-z5fcl4 {
            padding-top: 3rem;
        }

        /* Mengubah warna tombol "Sign Up" dan "Get Started!" */
        .stButton > button.primary {
            background-color: #0d6efd; /* Warna biru */
            border-color: #0d6efd; /* Warna border biru */
            color: white; /* Warna teks putih */
        }
        .stButton > button.primary:hover {
            background-color: #0b5ed7; /* Warna biru sedikit lebih gelap saat hover */
            border-color: #0b5ed7;
        }

        /* Mengubah warna tombol "Login" (yang default) */
        .stButton > button:not(.primary) {
            background-color: transparent; /* Transparan */
            border: 1px solid #0d6efd; /* Border biru */
            color: #0d6efd; /* Teks biru */
        }
        .stButton > button:not(.primary):hover {
            background-color: #0d6efd; /* Background biru saat hover */
            color: white; /* Teks putih saat hover */
        }
                
                /* --- Extract.py --- */

        /* Style file uploader agar tombolnya biru */
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
        /* Style teks label dropzone */
        .stFileUploader label {
        font-size: 1.1rem !important;
        font-weight: 500;
        color: #555; /* Warna abu-abu gelap */
        }

/* --- Akhir tambahan --- */
    </style>
    """, unsafe_allow_html=True)