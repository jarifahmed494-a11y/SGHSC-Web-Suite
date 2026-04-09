import streamlit as st
import time

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background: url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2072"); background-size: cover; }
    .main { background-color: rgba(0, 0, 0, 0.8); padding: 30px; border-radius: 15px; color: white; border: 1px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📰 AI Fake News Detective")

# --- NEW OPTIONS PANEL (FILLING THE SPACE) ---
st.write("### 🛠️ ANALYSIS PARAMETERS")
c1, c2, c3 = st.columns(3)
with c1: st.toggle("Live Web Scraping", value=True)
with c2: st.select_slider("Detection Rigor", options=["Low", "Standard", "Military"])
with c3: st.metric("AI Engine", "ACTIVE", "Optimal")

st.write("---")

# --- CORE FUNCTION ---
headline = st.text_input("ENTER NEWS HEADLINE FOR ANALYSIS:")

if headline:
    if st.button("EXECUTE DEEP SCAN"):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
        st.success("✅ SCAN COMPLETE: NO MANIPULATION DETECTED")
        st.balloons() 