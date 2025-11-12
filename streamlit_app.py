import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Strukify - Home",
    page_icon="🧾",  # Emoji struk
    layout="wide"  # Menggunakan layout lebar agar sesuai prototipe
)

# --- CSS KUSTOM ---
# Ini untuk membuat kotak biru bernomor dan mengatur beberapa padding
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
            
</style>
""", unsafe_allow_html=True)


# --- 1. HEADER ---
# Kita gunakan kolom untuk meniru logo di kiri dan tombol di kanan
col_logo, col_nav, col_login, col_signup = st.columns([2, 5, 1, 1])

with col_logo:
    # Menggunakan markdown untuk logo agar lebih besar dan berwarna
    st.markdown("<h1 style='color: #0d6efd;'>Strukify</h1>", unsafe_allow_html=True)

# Kolom tengah ini untuk navigasi (dijelaskan di bawah)
with col_nav:
    st.write("") # Kosongkan saja untuk sekarang

with col_login:
    # Tombol dibuat rata atas dengan tombol sign up
    st.write("<br>", unsafe_allow_html=True)
    st.button("Login", use_container_width=True)

with col_signup:
    st.write("<br>", unsafe_allow_html=True)
    st.button("Sign Up", type="primary", use_container_width=True)

st.divider()

# --- 2. HERO SECTION ---
with st.container():
    # Menggunakan markdown untuk membuat teks rata tengah
    st.markdown("<h1 style='text-align: center;'>Receipt Data</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Extractor & Analyzer</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; font-size: 1.1rem; max-width: 600px; margin: auto;'>
        Strukify helps you scan, extract, and analyze information from your shopping receipts in seconds. 
        Whether you're budgeting, recording purchases, or just curious where your money goes, Strukify makes it effortless.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("") # Memberi spasi
    
    # Trik untuk membuat tombol di tengah
    col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
    with col_btn2:
        st.button(
            "Get Started!", 
            type="primary", 
            help="Start extracting receipts!", 
            use_container_width=True
        )

st.write("<br><br><br>", unsafe_allow_html=True) # Memberi spasi besar

# --- 3. HOW IT WORKS (Grid 2x2) ---
col1, col2 = st.columns(2, gap="large")

# --- Kolom Kiri (Step 1 & 3) ---
with col1:
    with st.container():
        # Kotak biru dengan angka 1
        st.markdown('<span class="step-number">1</span>', unsafe_allow_html=True)
        st.subheader("Upload Your Receipt")
        st.write("Simply upload your receipt image by selecting the files. Strukify supports most common image formats (JPG, PNG, PNEG).")

    st.write("<br><br>", unsafe_allow_html=True) # Spasi antar step

    with st.container():
        # Kotak biru dengan angka 3
        st.markdown('<span class="step-number">3</span>', unsafe_allow_html=True)
        st.subheader("Review the Data")
        st.write("Preview the extracted table. You can edit or adjust any details before saving.")

# --- Kolom Kanan (Step 2 & 4) ---
with col2:
    with st.container():
        # Kotak biru dengan angka 2
        st.markdown('<span class="step-number">2</span>', unsafe_allow_html=True)
        st.subheader("Automatic Extraction")
        st.write("Our smart engine reads your receipt instantly by detecting store name, date, items, and total amount. No manual typing required.")

    st.write("<br><br>", unsafe_allow_html=True) # Spasi antar step
    
    with st.container():
        # Kotak biru dengan angka 4
        st.markdown('<span class="step-number">4</span>', unsafe_allow_html=True)
        st.subheader("Analyze & Save")
        st.write("View insights about your spending, export your data, or revisit it anytime in your History page.")