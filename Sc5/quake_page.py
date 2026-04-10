import streamlit as st
import numpy as np
import time

st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1510511459019-5ddd71426343?q=80&w=2000&auto=format&fit=crop"); background-size: cover; }
    .main { background-color: rgba(15, 0, 0, 0.9); padding: 30px; border-radius: 20px; border: 2px solid #ff4b4b; }
    h1 { color: #ff4b4b !important; text-shadow: 0px 0px 15px #ff4b4b; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# CORRECTED HEADER
c1, c2 = st.columns([3, 1])
with c1: st.caption("⚠️ TECTONIC SENSORS // SGHSC TECH LAB")
with c2: st.caption("🔴 SYSTEM: MONITORING")
st.write("---")

st.title("🌋 Seismic Tectonic Monitor")

m1, m2, m3 = st.columns(3)
m1.metric("Mag. Threshold", "4.5", "Alert Set")
m2.metric("Active Sensors", "84/84", "Online")
m3.metric("Uptime", "99.9%", "Stable")
st.write("---")

if st.button("EXECUTE LIVE SCAN"):
    chart_data = np.random.randn(20, 1)
    st.line_chart(chart_data)
    with st.spinner("Analyzing tectonic activity..."):
        time.sleep(2)
    st.error("AI ALERT: Low-frequency vibration detected.")# --- TOP UTILITY BAR ---
# This creates a row of buttons at the very top of your page
u1, u2, u3, u4 = st.columns([1, 1, 1, 4])
with u1: 
    if st.button("🏠 Home"): 
        st.rerun()
with u2:
    if st.button("⚙️ Config"): 
        st.toast("Security Clearance Required.", icon="🚫")
with u3:
    if st.button("🛠️ Tools"): 
        st.toast("Opening Forensic Toolkit...", icon="🧰")

st.write("---") # This line separates the buttons from your main content
