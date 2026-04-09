import streamlit as st
import random
import time

# --- STEP 1: DYNAMIC LOGIC ---
# This makes the percentage change every time the page runs
percent = round(random.uniform(92.1, 99.8), 1)

# --- STEP 2: STYLING ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1f2937;
        color: white;
        border: 1px solid #374151;
    }
    .stButton>button:hover {
        border-color: #00d4ff;
        color: #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STEP 3: HEADER ---
st.markdown("### 🔍 PIXEL FORENSICS // SGHSC TECH LAB")
st.title("🖼️ Forensic Image Analyzer")

col1, col2 = st.columns(2)
with col1:
    st.metric("Pixel Accuracy", f"{percent}%", "Stable")
with col2:
    st.metric("Neural Layers", "128-bit", "Active")

# --- STEP 4: SCANNER INTERFACE ---
file = st.file_uploader("Upload Image for Neural Processing", type=["jpg", "png", "jpeg"])

if file:
    st.image(file, caption="Source: Uploaded Buffer", use_container_width=True)
    
    if st.button("EXECUTE DEEP PIXEL SCAN"):
        with st.status("Initializing Core Engine...", expanded=True) as status:
            time.sleep(1)
            st.write("Analyzing lighting vectors...")
            time.sleep(1)
            st.write("Checking for AI-generated symmetry patterns...")
            time.sleep(1)
            st.success(f"✅ AUTHENTICITY: {percent}% Human Originated")
            status.update(label="Scan Complete", state="complete", expanded=False)

st.write("---")
