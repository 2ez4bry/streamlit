import streamlit as st
from streamlit_option_menu import option_menu

def render_header(current_page_index=0):
    """
    Merender header dengan logo dan navigasi horizontal.
    Menggunakan class CSS dari style.py.
    """
    
    col_logo, col_nav = st.columns([1, 4], vertical_alignment="center") 

    with col_logo:
        # PERUBAHAN: Sekarang kita pakai class='header-logo'
        # CSS-nya sudah diatur di style.py
        st.markdown(
            "<h2 class='header-logo'>Strukify</h2>", 
            unsafe_allow_html=True
        )

    with col_nav:
        # Style menu ini BIARKAN DISINI (jangan dipindah ke style.py)
        # karena library option_menu membutuhkannya sebagai parameter Python.
        selected = option_menu(
            menu_title=None,
            options=["Home", "Extract", "History", "About Us"],
            icons=["house-fill", "search", "clock-history", "info-circle-fill"],
            default_index=current_page_index,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "transparent",
                    "display": "flex",
                    "justify-content": "flex-end",
                    "padding-right": "20px !important" 
                }, 
                "icon": {"color": "#888", "font-size": "14px"}, 
                "nav-link": {
                    "font-size": "14px",
                    "font-weight": "600",
                    "color": "#888",
                    "margin": "0px 5px",
                    "--hover-color": "transparent"
                },
                "nav-link-selected": {
                    "background-color": "transparent",
                    "color": "#0d6efd",
                    "font-weight": "bold"
                },
            }
        )
    
    st.divider()
    
    # --- LOGIKA NAVIGASI ---
    if selected == "Home" and current_page_index != 0:
        st.switch_page("streamlit_app.py")
        
    elif selected == "Extract" and current_page_index != 1:
        st.switch_page("pages/Extract.py")
        
    elif selected == "History" and current_page_index != 2:
        st.switch_page("pages/History.py")
        
    elif selected == "About Us" and current_page_index != 3:
        st.switch_page("pages/AboutUs.py")