import streamlit as st
from streamlit_option_menu import option_menu

def render_header(default_index=0): # Kita tambahkan parameter default_index
    """
    Merender header dengan logo, navigasi horizontal, dan tombol login.
    """
    # Kolom tetap sama
    col_logo, col_nav, col_login, col_signup = st.columns([2, 5, 1, 1])

    with col_logo:
        st.markdown("<h1 style='color: #0d6efd;'>Strukify</h1>", unsafe_allow_html=True)

    with col_nav:
        # Beri sedikit jarak dari atas
        st.write("<br>", unsafe_allow_html=True) 
        
        # Ini adalah menu navigasi horizontal
        selected = option_menu(
            menu_title=None,  # Wajib ada, tapi kita kosongkan
            options=["Home", "Extract", "History", "Analysis"], # Sesuai prototipe
            icons=["house-fill", "search", "clock-history", "bar-chart-line-fill"], # Ikon opsional
            default_index=default_index,  # Halaman mana yang aktif
            orientation="horizontal",
            styles={
                # Style untuk container menu
                "container": {
                    "padding": "0!important", 
                    "background-color": "transparent",
                    "margin-top": "-10px" # Sesuaikan agar pas
                }, 
                # Style untuk ikon
                "icon": {"color": "#888", "font-size": "16px"}, 
                # Style untuk link
                "nav-link": {
                    "font-size": "16px",
                    "font-weight": "600",
                    "color": "#888", # Warna teks (abu-abu)
                    "text-align": "center",
                    "margin":"0px 8px",
                    "--hover-color": "#444" # Warna saat kursor di atas
                },
                # Style untuk link yang sedang aktif/dipilih
                "nav-link-selected": {
                    "background-color": "transparent",
                    "color": "white" # Warna teks (putih/terang)
                },
            }
        )
    
    # Tombol login/signup tetap sama
    with col_login:
        st.write("<br>", unsafe_allow_html=True)
        st.button("Login", use_container_width=True)

    with col_signup:
        st.write("<br>", unsafe_allow_html=True)
        st.button("Sign Up", type="primary", use_container_width=True)

    st.divider()
    
    # Kembalikan halaman mana yang diklik pengguna
    return selected