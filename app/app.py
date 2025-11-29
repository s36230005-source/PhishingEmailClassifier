import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_email

# ===== Page Config =====
st.set_page_config(
    page_title="Phishing Email Classifier",
    page_icon="🛡️",
    layout="centered"
)

# ===== Custom CSS =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.main {
    background-color: #f8f9fa;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 800px;
}

/* Header Section */
.header-section {
    background: #7d1935;
    padding: 3rem 2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 30px rgba(125, 25, 53, 0.2);
    text-align: center;
    animation: fadeInDown 0.6s ease-out;
}

.main-title {
    font-size: 3rem;
    font-weight: 700;
    color: white;
    margin: 0;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.subtitle {
    font-size: 1.15rem;
    color: rgba(255, 255, 255, 0.9);
    margin: 0;
    font-weight: 400;
}

/* Card Container */
.card {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e9ecef;
    animation: fadeInUp 0.6s ease-out;
}

.input-label {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2d3436;
    margin-bottom: 0.8rem;
    display: block;
}

/* Text Area Styling */
.stTextArea textarea {
    border: 2px solid #dee2e6;
    border-radius: 12px;
    padding: 1rem;
    font-size: 0.95rem;
    transition: all 0.3s ease;
    background-color: #f8f9fa;
    font-family: 'Poppins', sans-serif;
}

.stTextArea textarea:focus {
    border-color: #7d1935;
    box-shadow: 0 0 0 4px rgba(125, 25, 53, 0.1);
    background-color: white;
    outline: none;
}

/* Button Styling */
.stButton button {
    width: 100%;
    background-color: #7d1935;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(125, 25, 53, 0.3);
    margin-top: 1rem;
}

.stButton button:hover {
    background-color: #5e1327;
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(125, 25, 53, 0.4);
}

.stButton button:active {
    transform: translateY(0);
}

/* Result Boxes */
.result-box {
    margin-top: 2rem;
    padding: 2rem;
    border-radius: 16px;
    animation: slideIn 0.5s ease-out;
    border-left: 6px solid;
}

.result-phishing {
    background-color: #ffe8e8;
    border-left-color: #d63031;
}

.result-legitimate {
    background-color: #e8f8f5;
    border-left-color: #00b894;
}

.result-icon {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.result-label {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.label-phishing {
    color: #d63031;
}

.label-legitimate {
    color: #00b894;
}

.confidence-score {
    font-size: 1.1rem;
    color: #495057;
    font-weight: 500;
    margin-top: 0.5rem;
}

.confidence-bar-container {
    width: 100%;
    height: 8px;
    background-color: rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    margin-top: 1rem;
    overflow: hidden;
}

.confidence-bar {
    height: 100%;
    border-radius: 10px;
    transition: width 0.6s ease-out;
}

.bar-phishing {
    background-color: #d63031;
}

.bar-legitimate {
    background-color: #00b894;
}

/* Info Box */
.info-box {
    background-color: #fff5e6;
    border-left: 4px solid #7d1935;
    padding: 1.2rem 1.5rem;
    border-radius: 12px;
    margin-top: 2rem;
}

.info-text {
    color: #495057;
    font-size: 0.95rem;
    margin: 0;
    line-height: 1.6;
}

.info-icon {
    color: #7d1935;
    margin-right: 0.5rem;
}

/* Warning Box */
.stAlert {
    border-radius: 12px;
    border-left: 4px solid #f39c12;
}

/* Animations */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# ===== Header =====
st.markdown("""
<div class='header-section'>
    <div class='main-title'>🛡️ Phishing Email Classifier</div>
    <div class='subtitle'>Advanced AI-powered email security analysis</div>
</div>
""", unsafe_allow_html=True)

# ===== Main Card =====

st.markdown("<span class='input-label'>📧 Masukkan Teks Email</span>", unsafe_allow_html=True)
email_text = st.text_area(
    "Email content",
    height=250,
    placeholder="Paste konten email yang ingin Anda analisis di sini...",
    label_visibility="collapsed"
)

if st.button("🔍 Analisis Email"):
    if len(email_text.strip()) == 0:
        st.warning("⚠️ Silakan masukkan isi email terlebih dahulu.")
    else:
        with st.spinner("Menganalisis email..."):
            label, prob = predict_email(email_text)
            
            prob_percent = prob * 100
            
            if label == "Phishing":
                st.markdown(f"""
                <div class='result-box result-phishing'>
                    <div class='result-icon'>🚨</div>
                    <div class='result-label label-phishing'>Phishing Terdeteksi</div>
                    <div class='confidence-score'>Confidence Score: {prob:.4f} ({prob_percent:.2f}%)</div>
                    <div class='confidence-bar-container'>
                        <div class='confidence-bar bar-phishing' style='width: {prob_percent}%'></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-box result-legitimate'>
                    <div class='result-icon'>✅</div>
                    <div class='result-label label-legitimate'>Email Legitimate</div>
                    <div class='confidence-score'>Confidence Score: {prob:.4f} ({prob_percent:.2f}%)</div>
                    <div class='confidence-bar-container'>
                        <div class='confidence-bar bar-legitimate' style='width: {prob_percent}%'></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== Footer Info =====
st.markdown("""
<div class='info-box'>
    <p class='info-text'>
        <span class='info-icon'>🤖</span><strong>Teknologi:</strong> Model berbasis Random Forest dengan TF-IDF vectorization<br>
        <span class='info-icon'>🎯</span><strong>Tujuan:</strong> Mendeteksi email phishing secara otomatis untuk melindungi pengguna<br>
        <span class='info-icon'>⚡</span><strong>Akurasi:</strong> Model telah dilatih dengan ribuan sampel email untuk hasil terbaik
    </p>
</div>
""", unsafe_allow_html=True)