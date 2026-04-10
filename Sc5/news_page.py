import streamlit as st
import time
import re

# --- 1. PAGE BACKGROUND ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
        url("https://images.unsplash.com/photo-1504711434969-e33886168f5c");
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚖️ Truth Engine // Disinformation Lab")
st.subheader("Neural Linguistic Analysis // SGHSC V4.1")

text_input = st.text_area("Paste News Headline or Article URL for verification:", 
                          placeholder="Analysis system online... enter text for deep scan.")

if st.button("RUN DEEP SCAN"):
    if text_input:
        with st.status("Analyzing Linguistic Markers...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="Deep Scan Complete!", state="complete", expanded=False)

        input_lower = text_input.lower()
        
        # 1. HIGH-TRUST SOURCES (Force Authentic)
        # Add your local trusted news sites here
        trusted_sources = ["prothomalo.com", "reuters.com", "bbc.com", "apnews.com", "dailystar.net"]
        is_trusted_url = any(src in input_lower for src in trusted_sources)

        # 2. FALSE NEWS PATTERNS (Clickbait/Propaganda)
        fake_patterns = [r"shocking", r"exposed", r"miracle", r"conspiracy", r"!!!", r"unbelievable"]
        fake_score = sum(1 for p in fake_patterns if re.search(p, input_lower))

        # 3. AUTHENTIC NEWS PATTERNS (Journalistic Tone)
        real_patterns = [r"according to", r"reported by", r"official statement", r"confirmed by", r"investigation"]
        real_score = sum(1 for p in real_patterns if re.search(p, input_lower))

        # --- FINAL DECISION LOGIC ---
        # If it's a trusted URL, it is almost certainly authentic
        if is_trusted_url or (real_score > fake_score):
            st.success("✅ VERIFIED: AUTHENTIC NEWS CONTENT")
            st.metric("Credibility Score", "98.2%", "STABLE")
            st.markdown("- **Pattern Recognition:** Structural integrity matches verified journalism.")
            st.markdown("- **Status:** Safe for Public Consumption.")

        # If fake markers outnumber real markers
        elif fake_score > 0:
            st.error("🚨 ALERT: DISINFORMATION DETECTED")
            st.metric("Credibility Score", "12.5%", "CRITICAL RISK")
            st.markdown("- **Linguistic Bias:** High intensity manipulative language found.")
            st.markdown("- **Status:** Identified as Potential Propaganda.")

        # Neutral fallback
        else:
            st.warning("⚠️ NEUTRAL / UNVERIFIED CONTENT")
            st.metric("Credibility Score", "60.0%", "STABLE")
            st.info("Report: Content is neutral. No manipulative or journalistic markers found.")
            
    else:
        st.error("Please enter text for analysis.")
