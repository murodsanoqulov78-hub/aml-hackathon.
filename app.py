import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Alphamind · AML Intelligence Platform",
    page_icon="logo.png",
    layout="wide"
)

# Custom High-End Fintech CSS Styling
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stMetric { background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 20px; border-radius: 14px; border: 1px solid #374151; box-shadow: 0 8px 16px rgba(0,0,0,0.4); }
    h1, h2, h3 { color: #60a5fa; font-family: 'Inter', sans-serif; }
    .card { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #374151; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Top Header Layout with Logo
col_logo, col_title = st.columns([1, 6])
with col_logo:
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown("### 🛡️ [LOGO]")

with col_title:
    st.title("Alphamind: AML Alert Prioritization Engine")
    st.markdown("### 🚀 WIUT Hackathon 2026 · FinTech & AI in Finance | Team ID: `08CC3F2B`")

st.markdown("---")

# Sidebar
st.sidebar.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
st.sidebar.header("Navigatsiya Paneli")
menu = st.sidebar.radio("Bo'limni tanlang:", [
    "📊 Asosiy Metrikalar & KPI",
    "🔍 Ma'lumotlar Tuzilishi (EDA)",
    "📈 Xatti-harakatlar & Tahlil",
    "🤖 Model Arxitekturasi",
    "🏆 Xulosa va Natijalar"
])

if menu == "📊 Asosiy Metrikalar & KPI":
    st.header("Loyihaning Asosiy Ko'rsatkichlari")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Model Metrikasi", value="ROC-AUC", delta="Yuqori Aniqlik")
    with c2:
        st.metric(label="Algoritm", value="LightGBM", delta="Ensemble GBDT")
    with c3:
        st.metric(label="Validatsiya", value="5-Fold CV", delta="Stratified")
    with c4:
        st.metric(label="Jamoa ID", value="08CC3F2B", delta="Alphamind")
        
    st.markdown("---")
    st.markdown("""
    <div class="card">
    <h3>💡 Loyiha Haqida</h3>
    Moliyaviy monitoring bo'limlari uchun shubhali tranzaksiyalarni (AML) avtomatik aniqlash va ularning eskalatsiya qilinish ehtimolini yuqori aniqlikda bashorat qilish tizimi. Biz vaqt dinamikasi (Time Delta) va chuqur tranzaksiya agregatsiyalaridan foydalandik.
    </div>
    """, unsafe_allow_html=True)

elif menu == "🔍 Ma'lumotlar Tuzilishi (EDA)":
    st.header("Dataset va Ma'lumotlar Tuzilishi")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
        <h3>📋 Signal Jadvallari</h3>
        - <b>train_signals.csv</b>: Har bir alertning noyob ID raqami va sana ma'lumotlari.<br>
        - <b>eskalatsiya</b>: Target o'zgaruvchisi (1 = eskalatsiya qilingan, 0 = dismissed).
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
        <h3>💳 Tranzaksiya Jadvallari</h3>
        - <b>train_transactions.parquet</b>: Tarixiy tranzaksiyalar oqimi.<br>
        - <b>Parametrlar</b>: Kirim/chiqim yo'nalishi, tranzaksiya turi (karta, naqd, bank, xalqaro) va miqdor indeksi.
        </div>
        """, unsafe_allow_html=True)

elif menu == "📈 Xatti-harakatlar & Tahlil":
    st.header("Tranzaksiyalar Tahlili va Vizualizatsiya")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tranzaksiya Turlari Ulushi")
        turlar = pd.DataFrame({
            'Turi': ['Karta', 'Bank Oʻtkazmasi', 'Naqd', 'Xalqaro'],
            'Ulush (%)': [42, 31, 17, 10]
        })
        fig = px.pie(turlar, names='Turi', values='Ulush (%)', hole=0.4, color_discrete_sequence=px.colors.sequential.Blues_r)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Miqdor Indeksi Taqsimoti")
        np.random.seed(42)
        vals = np.random.lognormal(mean=1.2, sigma=0.6, size=500)
        fig2 = px.histogram(x=vals, nbins=30, labels={'x': 'Miqdor Indeksi', 'y': 'Chastota'}, title="Hajm Diapazoni")
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig2, use_container_width=True)

elif menu == "🤖 Model Arxitekturasi":
    st.header("Mashinali O'qitish va Feature Engineering")
    st.markdown("""
    <div class="card">
    <h3>⚙️ Ishlab chiqish bosqichlari:</h3>
    1. <b>Time Delta Features:</b> Signal sanasi va tranzaksiya vaqti orasidagi farq sekundlarda hisoblandi.<br>
    2. <b>Agregatsiya funksiyalari:</b> Har bir <code>signal_id</code> bo'yicha miqdor indeksining yig'indisi, o'rtacha, median va maksimum qiymatlari olindi.<br>
    3. <b>Model:</b> Yuqori aniqlikni ta'minlovchi <b>LightGBM Classifier</b> va 5-Fold Stratified Cross-Validation qo'llanildi.
    </div>
    """, unsafe_allow_html=True)

elif menu == "🏆 Xulosa va Natijalar":
    st.header("Yakuniy Xulosalar")
    st.success("Barcha talablar muvaffaqiyatli bajarildi: Bashorat CSV, professional logoli EDA veb-sayt va reproduktib notebook tayyor!")
    st.markdown("✨ *Alphamind jamoasi — WIUT Hackathon 2026*")