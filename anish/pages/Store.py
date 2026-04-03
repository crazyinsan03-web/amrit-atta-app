import streamlit as st

# 1. Page Configuration (Sidebar hide karne ke liye)
st.set_page_config(page_title="Amrit Atta | Premium Store", layout="wide", initial_sidebar_state="collapsed")

# 2. Ultra-Luxury CSS (Sidebar Hider + New Stable Images)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@300;400;600&display=swap');

    /* Sidebar ko poora hide karne ke liye */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.95)), 
                    url("https://images.unsplash.com/photo-1473360123247-9827a2fb5986?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .store-title {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(to right, #4a370e, #8b6508);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 55px !important;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }

    .store-sub {
        font-family: 'Poppins', sans-serif;
        color: #8b6508;
        text-align: center;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 14px;
        margin-bottom: 50px;
    }

    .product-card {
        background: white;
        border-radius: 30px;
        text-align: center;
        border: 1px solid rgba(184, 134, 11, 0.2);
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        overflow: hidden;
        margin-bottom: 20px;
        height: 520px; /* Fixed height for symmetry */
    }

    .product-card:hover {
        transform: translateY(-10px);
        border: 1px solid #D4AF37;
        box-shadow: 0 20px 40px rgba(184,134,11,0.2);
    }

    .product-image {
        width: 100%;
        height: 220px;
        object-fit: cover;
    }

    .product-details { padding: 20px; }

    .product-name { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700; color: #2c2c2c; }
    .product-price { font-family: 'Poppins', sans-serif; font-size: 32px; color: #B38728; font-weight: 700; margin: 15px 0; }

    .stButton > button {
        background: #2c2c2c;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 20px;
        width: 100%;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #D4AF37;
    }

    /* Hide default Streamlit parts */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="store-title">OUR ORGANIC ATTA</h1>', unsafe_allow_html=True)
st.markdown('<p class="store-sub">Directly from Rajsamand Farms</p>', unsafe_allow_html=True)

if 'cart' not in st.session_state:
    st.session_state.cart = []

# New Stable Images (Failing images replaced with high-quality backups)
products = [
    {"id": "p1", "name": "Classic Amrit", "w": "5 KG", "p": 210, "img": "https://images.unsplash.com/photo-1594911772125-07fc7a2d8d9f?w=500"},
    {"id": "p2", "name": "Silver Amrit", "w": "10 KG", "p": 400, "img": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=500"},
    {"id": "p3", "name": "Gold Family", "w": "25 KG", "p": 950, "img": "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=500"},
    {"id": "p4", "name": "Premium Bran", "w": "2 KG", "p": 120, "img": "https://images.unsplash.com/photo-1501430460132-46653e2d1233?w=500"}
]

cols = st.columns(4)

for i, p in enumerate(products):
    with cols[i]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}" class="product-image">
                <div class="product-details">
                    <div class="product-name">{p['name']}</div>
                    <div style="color: #666; font-size: 14px;">Weight: {p['w']}</div>
                    <div class="product-price">₹{p['p']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"ADD TO CART", key=p['id']):
            st.session_state.cart.append(p)
            st.toast(f"{p['name']} added!")

# Checkout Section
if st.session_state.cart:
    st.write("---")
    if st.button("PROCEED TO CHECKOUT ➡️"):
        st.switch_page("pages/Checkout.py")