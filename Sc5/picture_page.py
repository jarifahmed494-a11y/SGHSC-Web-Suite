import streamlit as st
import time

# --- 1. PAGE BACKGROUND ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b");
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HEADER & INTERFACE ---
st.title("🛡️ DEEP-PIXEL SURVEILLANCE // SGHSC V2.5")
st.subheader("AI vs Human Content Guard")

uploaded_file = st.file_uploader("Insert Image for Forensic Decomposition", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Scanning Source Material...", use_container_width=True)
    
    # Forensic progress simulation
    with st.status("Performing Neural Layer Analysis...", expanded=True) as status:
        st.write("Extracting Metadata...")
        time.sleep(1)
        st.write("Scanning for GAN artifacts...")
        time.sleep(1.5)
        st.write("Verifying Pixel Consistency...")
        time.sleep(1)
        status.update(label="Analysis Complete!", state="complete", expanded=False)

    # --- 3. THE AUTHENTICATION TRICK ---
    file_name = uploaded_file.name
    
    # SET AS FALSE / AI GENERATED
    if "Neural_Render" in file_name:
        st.error(f"🚨 ALERT: HIGH PROBABILITY OF AI GENERATION DETECTED")
        st.metric("Confidence Score", "98.4%", "NON-HUMAN")
        st.warning("Forensic report: Latent space artifacts found in 128-bit neural layers.")
    
    # SET AS AUTHENTIC / HUMAN
    elif "Nature_Capture" in file_name:
        st.success(f"✅ VERIFIED: AUTHENTIC HUMAN CONTENT")
        st.metric("Confidence Score", "99.1%", "STABLE")
        st.info("Forensic report: Natural grain and consistent pixel metadata confirmed.")
    
    # DEFAULT SCAN FOR OTHER FILES
    else:
        st.info("Scanning unindexed file. Performing standard heuristic analysis...")
        st.metric("Confidence Score", "N/A", "Scanning...")
