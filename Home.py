import streamlit as st
from streamlit_option_menu import option_menu
from team_info import team_info

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="KrishiMitra", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    color: #2E8B57;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 20px;
}
.card {
    background: linear-gradient(145deg, #1e1e1e, #2a2a2a);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0 6px 15px rgba(0,0,0,0.3);
    cursor: pointer;
    margin: 8px;
}
.card:hover {
    background: linear-gradient(145deg, #2E8B57, #3CB371);
    color:white;
    transform: translateY(-5px) scale(1.03);
}
.card a {
    text-decoration: none;
    color: inherit;
}
.footer {
    text-align: center;
    font-size: 14px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="KrishiMitra",
        options=["Home", "Chatbot", "About"],
        icons=["house", "chat", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# ---------------- HEADER SECTION ----------------
st.markdown('<div class="main-title">🌾 KrishiMitra</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Smart Farming Platform</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- HOME PAGE ----------------
if selected == "Home":

    st.markdown("## 👋 Welcome to KrishiMitra")
    st.markdown("> *Empowering Farmers with Innovation and Intelligence*")

    st.markdown("""
    **KrishiMitra** is an all-in-one smart farming platform integrating  
    AI, Machine Learning, and Real-time Weather Intelligence  
    to support farmers in making better agricultural decisions.
    """)

    # -------- FEATURE CARDS --------
    st.markdown("### 🚀 Core Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <a href="/disease_detection" target="_self">
                🌿 <h3>Disease Detection</h3>
                <p>AI-based crop disease analysis</p>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <a href="/crop_recommendation" target="_self">
                🌾 <h3>Crop Recommendation</h3>
                <p>Best crops based on soil & climate</p>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <a href="/fertilizer_suggestion" target="_self">
                💊 <h3>Fertilizer Suggestion</h3>
                <p>Smart fertilizer selection</p>
            </a>
        </div>
        """, unsafe_allow_html=True)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("""
        <div class="card">
            <a href="/action_advisory" target="_self">
                🌦️ <h3>Weather Advisory</h3>
                <p>Real-time insights for farmers</p>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="card">
            <a href="/chatbot" target="_self">
                🤖 <h3>AI Chatbot</h3>
                <p>Ask anything about farming</p>
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
# ---------------- CHATBOT ----------------
elif selected == "Chatbot":
    st.switch_page("pages/chatbot.py")

# ---------------- ABOUT PAGE ----------------
elif selected == "About":

    st.markdown("## ➤➤About Project")

    st.write("""
    **KrishiMitra** is an AI-powered smart farming web platform developed by a dedicated team from **PCE Purnea** .  

It integrates **Machine Learning, Deep Learning, and Real-Time Weather Intelligence** to assist farmers in making data-driven agricultural decisions.  

The platform provides:
- 🌿 Crop Disease Detection using Deep Learning  
- 🌾 Crop Recommendation based on soil & climate conditions  
- 💊 Fertilizer Suggestion System  
- 🌦️ Real-time Weather-based Agricultural Advisory  
- 🤖 AI Chatbot for instant farming guidance  

This project is developed under the guidance of **Prof. Supriya Kumari**, whose mentorship played a crucial role in shaping the system design, model optimization, and practical implementation.

    """)

    st.markdown("### Mission")
    st.write("""
    To empower farmers through:
    - 🌐 Modern technology  
    - 📊 Data-driven insights  
    - 🌿 Sustainable agriculture  
    """)

    # -------- TEAM --------
    st.markdown("### 👨‍💻 Team Members")

    def create_tooltip(name):
        return f"""
        <span title="{team_info[name]}" style="cursor:pointer; color:#2E8B57; font-weight:bold;">
            {name}
        </span>
        """

    st.markdown(f"""
    - {create_tooltip("Arpita kumari(22151131024)")}  
    - {create_tooltip("Om Shankar kumar(22151131019)")}  
    - {create_tooltip("Priya kumari(23151131902)")}  
    - {create_tooltip("Shubham kumar(22151131009)")}  
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>© 2026 KrishiMitra | Smart Farming Platform</p>",
    unsafe_allow_html=True
)