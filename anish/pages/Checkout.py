import streamlit as st
import requests
import json

# 1. Page Configuration
st.set_page_config(page_title="Amrit Atta | Premium Checkout", layout="centered")

# --- YAHAN APNA GOOGLE SCRIPT URL PASTE KAREIN ---
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw2x9WY9ZzRpqGhT0gb6_gY_tX85eGQM2QrkGynkESMg0syBKSYKjdcdHbhUrqhtPK9Jg/exec"
# 2. Premium Light CSS (Ivory, Champagne Gold & Charcoal)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@300;400;600&display=swap');
    
    [data-testid="stSidebar"] { display: none; }
    
    /* Soft Ivory Background */
    .stApp {
        background: #fdfbf7;
        color: #2c2c2c;
    }
    
    /* Luxury Floating Card */
    .checkout-container {
        background: white;
        padding: 50px;
        border-radius: 40px;
        box-shadow: 0 30px 70px rgba(184, 134, 11, 0.1);
        border: 1px solid #eee8d5;
        margin-top: 20px;
    }
    
    .elite-title {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(to right, #8b6508, #b38728);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px !important;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .elite-sub {
        font-family: 'Poppins', sans-serif;
        color: #8b6508;
        text-align: center;
        letter-spacing: 5px;
        font-size: 11px;
        text-transform: uppercase;
        margin-bottom: 40px;
        opacity: 0.7;
    }

    /* Summary Box with Soft Gold Tint */
    .summary-card {
        background: #fffcf5;
        border: 1px dashed #d4af37;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 35px;
        text-align: center;
    }

    /* Clean Input Fields */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #ffffff !important;
        color: #2c2c2c !important;
        border: 1px solid #ddd !important;
        border-radius: 15px !important;
        padding: 12px !important;
        transition: 0.3s;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.1) !important;
    }
    
    /* The Signature Gold Button */
    .stButton > button {
        background: linear-gradient(135deg, #B38728 0%, #8b6508 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 20px !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 18px;
        border: none;
        width: 100%;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 10px 25px rgba(139, 101, 8, 0.2);
        margin-top: 15px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(139, 101, 8, 0.4);
        filter: brightness(1.1);
    }

    .success-msg {
        background: #f0fdf4;
        color: #166534;
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        border: 1px solid #bbf7d0;
        font-family: 'Poppins', sans-serif;
        margin-top: 20px;
    }

    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. Main Layout
st.markdown('<div class="checkout-container">', unsafe_allow_html=True)
st.markdown('<h1 class="elite-title">Checkout</h1>', unsafe_allow_html=True)
st.markdown('<p class="elite-sub">Premium Quality Assured</p>', unsafe_allow_html=True)

# Logic: Empty Cart
if 'cart' not in st.session_state or len(st.session_state.cart) == 0:
    st.info("Aapki cart khali hai.")
    if st.button("⬅️ STORE PAR JAYEIN"):
        st.switch_page("pages/Store.py")
    st.stop()

# 4. Summary Card
total_val = sum(item.get('p', 0) for item in st.session_state.cart)
items_val = ", ".join([f"{i.get('name')} ({i.get('w')})" for i in st.session_state.cart])

st.markdown('<div class="summary-card">', unsafe_allow_html=True)
st.markdown(f"<p style='color:#8b6508; font-size:13px; margin-bottom:5px; font-weight:600;'>ORDER SUMMARY</p>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color:#333; margin-bottom:10px;'>{items_text if 'items_text' in locals() else items_val}</h4>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color:#B38728; margin:0;'>Total: ₹{total_val}</h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Professional Form
st.markdown("<p style='color:#666; font-size:14px; margin-bottom:20px; font-weight:600;'>🚚 DELIVERY DETAILS</p>", unsafe_allow_html=True)
with st.form("light_elite_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        name_in = st.text_input("Aapka Naam")
    with c2:
        phone_in = st.text_input("WhatsApp Number")
    
    addr_in = st.text_area("Pura Pata (Kankroli/Rajsamand)")
    
    st.markdown("<p style='font-size:12px; color:#888;'>Paisa delivery ke waqt dena hai (Cash on Delivery).</p>", unsafe_allow_html=True)
    
    submit_btn = st.form_submit_button("PLACE ORDER NOW")

    if submit_btn:
        if name_in and phone_in and addr_in:
            data_packet = {
                "name": name_in,
                "phone": phone_in,
                "address": addr_in,
                "items": items_val,
                "total": total_val
            }
            
            if GOOGLE_SCRIPT_URL != "YOUR_APPS_SCRIPT_URL_HERE":
                try:
                    res = requests.post(GOOGLE_SCRIPT_URL, data=json.dumps(data_packet))
                    if res.status_code == 200:
                        st.balloons()
                        st.markdown(f"""
                            <div class="success-msg">
                                <h3 style="margin:0;">🎊 Order Lag Gaya!</h3>
                                <p>Dhanyawad {name_in}, hum jald hi aapke pate par Amrit Atta pahunchayenge.</p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.session_state.cart = []
                    else:
                        st.error("Sheet Connection Error!")
                except:
                    st.error("Network Problem!")
            else:
                st.warning("⚠️ Google Script URL missing hai!")
        else:
            st.error("Bhai, details toh bhar do!")

st.markdown('</div>', unsafe_allow_html=True)
