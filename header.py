import streamlit as st

def render_header():
    """
    Fungsi untuk merender header aplikasi dengan logo dan tombol login/signup.
    """
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