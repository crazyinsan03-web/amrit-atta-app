import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Basic Page Setup
st.set_page_config(page_title="Amrit Atta | Premium Organic", layout="centered")

# 2. Lottie Animation Load (Wheat Animation)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_wheat = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m6cu96ze.json")

# 3. Ultra-Luxury CSS (Golden Theme + Glassmorphism)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@300;400;600&display=swap');

    /* Background: Professional Wheat Field with Dark Overlay */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Glassmorphism Main Card */
    .main-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 40px;
        padding: 60px 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        text-align: center;
        margin-top: 10px;
    }

    /* Luxury Gold Title */
    .luxury-title {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: clamp(45px, 10vw, 85px) !important;
        font-weight: 900;
        margin-bottom: 0px;
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));
    }

    /* Local Touch: Apno Rajsamand */
    .local-touch {
        font-family: 'Poppins', sans-serif;
        color: #D4AF37; 
        font-size: 28px !important;
        font-weight: 600;
        margin-top: -20px;
        margin-bottom: 10px;
        letter-spacing: 1px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    .luxury-sub {
        font-family: 'Poppins', sans-serif;
        color: #f1f1f1;
        font-size: 18px !important;
        font-weight: 300;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }

    /* 3D Golden Button for Mobile Users */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #8b6508 100%);
        color: white !important;
        border: none;
        padding: 25px 50px;
        font-size: 24px !important;
        font-weight: 700 !important;
        border-radius: 60px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.4);
        width: 100%;
        text-transform: uppercase;
        cursor: pointer;
    }

    .stButton > button:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px rgba(212, 175, 55, 0.6);
    }

    /* Clean UI: Hide default Streamlit parts */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 4. App Layout
st.write("") # Top Spacing

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Gold Brand Title
    st.markdown('<h1 class="luxury-title">AMRIT ATTA</h1>', unsafe_allow_html=True)
    
    # Local Branding
    st.markdown('<p class="local-touch">🚩 अपणो राजसमंद</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="luxury-sub">Pure. Fresh. Traditional.</p>', unsafe_allow_html=True)
    
    # Wheat Animation (Center)
    if lottie_wheat:
        st_lottie(lottie_wheat, height=320, key="wheat_main")
    
    st.write("")
    
    # Call to Action: Store Link
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        if st.button("🛒 EXPLORE STORE"):
            st.switch_page("pages/Store.py")
            
    st.markdown('</div>', unsafe_allow_html=True)

# 5. Luxury Footer
st.markdown("""
<div style="text-align: center; margin-top: 60px; font-family: 'Poppins'; color: #f1f1f1; font-size: 14px; opacity: 0.8;">
    🌾 Directly from the farms of Rajsamand to your kitchen. ✨
</div>
""", unsafe_allow_html=True)