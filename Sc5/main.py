import streamlit as st
import base64
import os

# 1. Page Configuration
st.set_page_config(page_title="SGHSC Social Response Center 9E", layout="wide", initial_sidebar_state="expanded")

# 2. Advanced CSS for High-Density Interface
def apply_final_styles(logo_path):
    encoded = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            
    st.markdown(f"""
        <style>
        [data-testid="stHeader"] {{ background-color: rgba(0,0,0,0); }}
        
        /* SIDEBAR LOGO FIX */
        [data-testid="stSidebar"] {{
            background-image: url("data:image/png;base64,{encoded}");
            background-repeat: no-repeat;
            background-position: 20px 98%;
            background-size: 65px 65px;
            background-color: #0e1117;
        }}

        /* THE FIX: Button Row Styling */
        .stButton > button {{
            width: 100% !important;
            background-color: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid #333 !important;
            color: #eeeeee !important;
            font-size: 11px !important;
            font-family: 'Courier New', monospace;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 5px !important;
            border-radius: 4px;
            white-space: nowrap !important; /* Prevents words from breaking */
        }}
        
        .stButton > button:hover {{
            border-color: #00d4ff !important;
            color: #00d4ff !important;
            background-color: rgba(0, 212, 255, 0.1) !important;
        }}

        /* System Info Text */
        .system-info {{
            text-align: right;
            color: #00d4ff;
            font-family: monospace;
            font-size: 10px;
            line-height: 1.2;
            padding-top: 5px;
        }}
        </style>
    """, unsafe_allow_html=True)

apply_final_styles("sghsc-logo.png")

# --- STEP 1: DENSE NAVIGATION BAR (Fills Blank Space) ---
# We use more columns to spread the buttons and info across the full width
nav_cols = st.columns([1, 1, 1, 1.2, 1.2, 1, 1, 3]) # Increased space for Registry/Network

with nav_cols[0]: 
    st.button("HOME")
with nav_cols[1]: 
    st.button("CONFIG")
with nav_cols[2]: 
    st.button("TOOLS")
with nav_cols[3]: 
    st.button("REGISTRY") # Dedicated wider column
with nav_cols[4]: 
    st.button("NETWORK")  # Dedicated wider column
with nav_cols[5]: 
    st.button("LOGS")
with nav_cols[6]: 
    st.button("EXIT")
with nav_cols[7]:
    # This fills the "Blank" space on the right with cool system data
    st.markdown("""
        <div class="system-info">
            TERMINAL: GRV-9E-MAINFRAME<br>
            SECURE_UPLINK: ACTIVE [AES-256]<br>
            CORE_SYNC: OPTIMAL
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- STEP 2: DYNAMIC SYSTEM METRICS ---
# Restoring the metrics that made the original workstation look "full"
m1, m2, m3, m4 = st.columns(4)
m1.metric("CPU LOAD", "42%", "Normal")
m2.metric("NEURAL SYNC", "98.9%", "Stable")
m3.metric("SERVER UPTIME", "742H", "+2.1%")
m4.metric("DATA TRAFFIC", "1.2 GB/s", "Active")

# --- STEP 3: HEADER ---
logo_path = "sghsc-logo.png"
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        h_enc = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 20px; padding: 15px 0; border-bottom: 2px solid #00d4ff;">
            <img src="data:image/png;base64,{h_enc}" width="65">
            <div>
                <h1 style="color: white; margin: 0; font-size: 22px; letter-spacing: 2px;">SGHSC STUDENTS WEB</h1>
                <p style="color: #00d4ff; margin: 0; font-size: 12px; font-family: monospace;">INTELLIGENT SOCIAL RESPONSE MAINFRAME // V4.2.0</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- STEP 4: SIDEBAR & NAVIGATION ---
with st.sidebar:
    st.write("### 🛠️ LIVE CONSOLE")
    st.status("System Optimal", state="complete")
    st.write("---")

pg = st.navigation([
    st.Page("picture_page.py", title="Forensic Image Analyzer", icon="🖼️"),
    st.Page("traffic_page.py", title="Urban Traffic AI", icon="🚦"),
    st.Page("quake_page.py", title="Seismic Monitor", icon="⚠️"),
    st.Page("news_page.py", title="Truth Engine", icon="📰")
])
pg.run()
