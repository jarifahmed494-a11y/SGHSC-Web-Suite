import streamlit as st
import base64
import os

# 1. Page Configuration
st.set_page_config(page_title="SGHSC Social Response Center 9E", layout="wide", initial_sidebar_state="expanded")

# 2. Ultra-Clean CSS (Fixed for Sidebar Arrow)
def apply_final_styles(logo_path):
    encoded = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            
    st.markdown(f"""
        <style>
        /* This hides the top colored line but KEEPS the sidebar arrow visible */
        [data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0);
            color: white;
        }}
        
        .main .block-container {{padding-top: 1rem;}}
        
        /* SIDEBAR LOGO (Bottom Left) */
        [data-testid="stSidebar"] {{
            background-image: url("data:image/png;base64,{encoded}");
            background-repeat: no-repeat;
            background-position: 20px 98%;
            background-size: 60px 60px;
            background-color: #0e1117;
        }}
        
        /* Remove button boxes and emojis style for Top Nav */
        div.stButton > button {{
            background: none !important;
            border: none !important;
            color: #eeeeee !important;
            padding: 0 !important;
            font-size: 13px !important;
            font-weight: 400 !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        div.stButton > button:hover {{
            color: #00d4ff !important;
            text-decoration: underline !important;
        }}
        </style>
    """, unsafe_allow_html=True)

apply_final_styles("sghsc-logo.png")

# --- STEP 1: ALL-IN-ONE TOP NAVIGATION (No Emojis) ---
cols = st.columns([0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 4])

with cols[0]: 
    if st.button("HOME"): st.toast("Home Loaded")
with cols[1]: 
    if st.button("CONFIG"): st.sidebar.info("Admin Settings: Active")
with cols[2]: 
    if st.button("TOOLS"): st.sidebar.write("Diagnostic Suite: Ready")
with cols[3]: 
    if st.button("REGISTRY"): st.sidebar.write("Student Records: Secure")
with cols[4]: 
    if st.button("NETWORK"): st.sidebar.success("Signal: 100%")
with cols[5]: 
    if st.button("LOGS"): st.sidebar.code("SESSION_START: 2026-04-09")
with cols[6]: 
    if st.button("EXIT"): st.stop()
with cols[7]:
    st.markdown("<p style='text-align:right; color:#555; font-size:11px;'>SGHSC_SECURE_MAINFRAME_v2.4</p>", unsafe_allow_html=True)

# --- STEP 2: BRANDED HEADER ---
logo_path = "sghsc-logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        h_enc = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 20px; padding: 15px 0; border-bottom: 1px solid #333;">
            <img src="data:image/png;base64,{h_enc}" width="70" style="border-radius:50%; border:1px solid #00d4ff;">
            <div>
                <h1 style="color: white; margin: 0; font-size: 24px;">SGHSC STUDENTS WEB</h1>
                <p style="color: #00d4ff; margin: 0; font-size: 14px; font-family: monospace;">SOCIAL RESPONSE CENTER</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- STEP 3: SIDEBAR CONSOLE ---
with st.sidebar:
    st.write("### 🛠️ LIVE CONSOLE")
    st.status("System Optimal", state="complete")
    st.write("---")

# --- STEP 4: PAGE NAVIGATION ---
pg = st.navigation([
    st.Page("picture_page.py", title="Forensic Image Analyzer", icon="🖼️"),
    st.Page("traffic_page.py", title="Urban Traffic AI", icon="🚦"),
    st.Page("quake_page.py", title="Seismic Monitor", icon="⚠️"),
    st.Page("news_page.py", title="Truth Engine", icon="📰")
])
pg.run()
