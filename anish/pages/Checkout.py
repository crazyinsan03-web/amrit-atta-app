import streamlit as st
import requests
import json
from streamlit_js_eval import streamlit_js_eval

# 1. Page Configuration
st.set_page_config(page_title="Amrit Atta | Premium Checkout", layout="centered")

# --- APNA GOOGLE SCRIPT URL ---
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw2x9WY9ZzRpqGhT0gb6_gY_tX85eGQM2QrkGynkESMg0syBKSYKjdcdHbhUrqhtPK9Jg/exec"

# 2. Premium CSS (Wahi purana luxury look)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@300;400;600&display=swap');
    [data-testid="stSidebar"] { display: none; }
    .stApp { background: #fdfbf7; color: #2c2c2c; }
    .checkout-container { background: white; padding: 40px; border-radius: 30px; box-shadow: 0 20px 50px rgba(184, 134, 11, 0.1); border: 1px solid #eee8d5; }
    .elite-title { font-family: 'Playfair Display', serif; background: linear-gradient(to right, #8b6508, #b38728); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 42px !important; text-align: center; margin-bottom: 0; }
    .elite-sub { font-family: 'Poppins', sans-serif; color: #8b6508; text-align: center; letter-spacing: 4px; font-size: 10px; text-transform: uppercase; margin-bottom: 30px; opacity: 0.7; }
    .summary-card { background: #fffcf5; border: 1px dashed #d4af37; padding: 20px; border-radius: 20px; margin-bottom: 30px; text-align: center; }
    .stButton > button { background: linear-gradient(135deg, #B38728 0%, #8b6508 100%) !important; color: white !important; border-radius: 50px !important; font-weight: 700; width: 100%; transition: 0.4s; }
    .loc-btn > div > button { background: #f0f0f0 !important; color: #333 !important; border: 1px solid #ccc !important; font-size: 12px !important; }
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="checkout-container">', unsafe_allow_html=True)
st.markdown('<h1 class="elite-title">Checkout</h1>', unsafe_allow_html=True)
st.markdown('<p class="elite-sub">Premium Quality Assured</p>', unsafe_allow_html=True)

# Check for Empty Cart
if 'cart' not in st.session_state or len(st.session_state.cart) == 0:
    st.info("Aapki cart khali hai.")
    if st.button("⬅️ STORE PAR JAYEIN"): st.switch_page("pages/Store.py")
    st.stop()

# 3. Order Summary
total_val = sum(item.get('p', 0) for item in st.session_state.cart)
items_val = ", ".join([f"{i.get('name')} ({i.get('w')})" for i in st.session_state.cart])

st.markdown('<div class="summary-card">', unsafe_allow_html=True)
st.markdown(f"<h2 style='color:#B38728; margin:0;'>Total: ₹{total_val}</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#555;'>{items_val}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. LOCATION FEATURE (Hybrid)
st.markdown("### 📍 Delivery Address")
col1, col2 = st.columns([2, 1])

with col2:
    st.write("") # Padding
    if st.button("🎯 Get Live Location", help="Browser aapse permission maangega, Allow karein"):
        loc = streamlit_js_eval(data_string='navigator.geolocation.getCurrentPosition(s => {window.dispatchEvent(new CustomEvent("location", {detail: (({latitude, longitude}) => ({latitude, longitude}))(s.coords)}));});', key='get_loc')
        if loc:
            lat, lon = loc['latitude'], loc['longitude']
            st.session_state.auto_addr = f"https://www.google.com/maps?q={lat},{lon}"
            st.toast("Location Captured! ✅")

# 5. Form
with st.form("delivery_form"):
    u_name = st.text_input("Aapka Naam", placeholder="Full Name")
    u_phone = st.text_input("WhatsApp Number", placeholder="91XXXXXXXX")
    
    # Auto-fill address if location captured, else empty
    current_addr = st.session_state.get('auto_addr', "")
    u_address = st.text_area("Full Address / Location Link", value=current_addr, placeholder="Ghar ka pata ya Landmark likhein...")
    
    st.info("Paisa delivery ke waqt dena hai (Cash on Delivery).")
    submit = st.form_submit_button("PLACE ORDER NOW")

    if submit:
        if u_name and u_phone and u_address:
            data = {
                "name": u_name,
                "phone": u_phone,
                "address": u_address,
                "items": items_val,
                "total": total_val
            }
            try:
                res = requests.post(GOOGLE_SCRIPT_URL, data=json.dumps(data))
                if res.status_code == 200:
                    st.balloons()
                    st.success(f"🎊 Order Successfully Lag Gaya! Dhanyawad {u_name}.")
                    st.session_state.cart = []
                    if 'auto_addr' in st.session_state: del st.session_state.auto_addr
                else:
                    st.error("Sheet Connection Error! Check Settings.")
            except:
                st.error("Network Problem! Please try again.")
        else:
            st.warning("Bhai, saari details bharna zaroori hai!")

st.markdown('</div>', unsafe_allow_html=True)
