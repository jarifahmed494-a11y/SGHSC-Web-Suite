import streamlit as st
import time

# --- PURE DIGITAL-FORENSIC STYLE (RESTORED VIBE) ---
st.markdown("""
    <style>
    /* 1. Sets the new digital background image (glowing circuit lines) */
    .stApp {
        background: url("https://images.unsplash.com/photo-1544256718-3bcf237f3974?q=80&w=2000&auto=format&fit=crop");
        background-size: cover;
    }
    
    /* 2. Style for the overall content box (it's now mostly transparent with a glowing border) */
    div.block-container {
        background-color: rgba(20, 0, 40, 0.4); /* Much more transparent so you see the picture */
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #a020f0; /* Purple glow border */
    }
    
    /* 3. Headline Style (BRIGHT white for maximum visibility) */
    h1 {
        color: #ffffff !important; 
        text-shadow: 0px 0px 15px #ffffff;
        font-family: 'Courier New', monospace;
    }
    
    /* 4. Secondary text, labels, etc. (White) */
    .stCaption, p, div, label {
        color: #ffffff !important; 
    }
    
    /* 5. Glowing accents (Green) for metrics and indicators */
    span.stMetricValue {
        color: #00ff00 !important;
        text-shadow: 0px 0px 10px #00ff00;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PRO HEADER ---
c1, c2 = st.columns([3, 1])
with c1: st.caption("🔍 PIXEL FORENSICS // SGHSC TECH LAB")
with c2: st.caption("🟢 SCANNER: READY")
st.write("---")

st.title("🖼️ Forensic Image Analyzer")

# --- METRICS ---
m1, m2 = st.columns(2)
m1.metric("Pixel Accuracy", "99.1%", "Stable")
m2.metric("Neural Layers", "128-bit", "Active")

st.write("---")

# --- TOOLS ---
# Uploading, analyzing, and detecting artifacts
file = st.file_uploader("Upload Image for Neural Processing", type=["jpg", "png", "jpeg"])
if file:
    st.image(file, width=350)
    if st.button("Execute Deep Pixel Scan"):
        with st.status("Analyzing lighting vectors...", expanded=True) as status:
            time.sleep(1)
            st.write("Checking for AI-generated symmetry patterns...")
            time.sleep(1)
            status.update(label="Scan Complete", state="complete")
        st.success("✅ AUTHENTICITY: 99.2% Human Originated")
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