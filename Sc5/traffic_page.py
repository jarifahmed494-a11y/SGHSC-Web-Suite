import streamlit as st
import random
import time

# --- PURE CYBER-TRAFFIC STYLE ---
# BACKGROUND CHANGE: The photo REMAINS THE SAME.
# TEXT BACKGROUND ADDITION: A dark semi-transparent box is added around all text content for readability.
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
    }
    div.block-container {
        background-color: rgba(0, 15, 30, 0.85); /* Dark semi-transparent cyan box for readability */
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #00d4ff; /* Cyan glow border */
    }
    h1 {
        color: #00d4ff !important;
        text-shadow: 0px 0px 15px #00d4ff;
        font-family: 'Courier New', monospace;
    }
    .stCaption, p, div, label {
        color: #ffffff !important; /* Pure white for secondary text */
    }
    </style>
    """, unsafe_allow_html=True)

# --- PRO HEADER ---
c1, c2 = st.columns([3, 1])
with c1: st.caption("🛰️ LIVE SATELLITE FEED // SGHSC TECH LAB")
with c2: st.caption("🟢 CORE: ONLINE")
st.write("---")

st.title("🚦 Urban Traffic Intelligence")

# --- METRICS ---
m1, m2, m3 = st.columns(3)
m1.metric("Flow Efficiency", "72%", "+5%")
m2.metric("Active Nodes", "1,204", "Stable")
m3.metric("Neural Confidence", "99.4%", "Optimal")

st.write("---")

if st.button("EXECUTE AREA SCAN"):
    with st.spinner("AI processing data streams..."):
        time.sleep(1.5)
        st.success("SCAN COMPLETE: NO GRIDLOCK DETECTED")
        with st.container(border=True):
            st.subheader("Traffic Analysis Report")
            st.code("Sector 7: Clear\nSector 4: Moderate Flow\nIntersection B: Optimizing Signal Timing...", language="bash")
            # --- TOP UTILITY BAR ---
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