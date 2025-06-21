import streamlit as st

# ------------------ 설정 ------------------
st.set_page_config(page_title="🌈 MBTI 직업 추천기", page_icon="💼", layout="wide")

# ------------------ 헤더 ------------------
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI로 찾는 나의 미래 직업 💫</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🧠 내 성격에 딱 맞는 직업을 찾아보자! ✨</h3>", unsafe_allow_html=True)
st.divider()

# ------------------ MBTI 목록 ------------------
mbti_types = [
    "INTJ 🧠", "INTP 🔬", "ENTJ 🦸", "ENTP 🎭",
    "INFJ 🌌", "INFP 🎨", "ENFJ 🤝", "ENFP 🌈",
    "ISTJ 📚", "ISFJ 🧸", "ESTJ 🧱", "ESFJ 🎀",
    "ISTP 🛠️", "ISFP 🌿", "ESTP 🚀", "ESFP 🎉"
]

# ------------------ 사용자 선택 ------------------
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", mbti_types)

# ------------------ 추천 데이터 ------------------
job_recommendations = {
    "INTJ 🧠": [
        ("📊 데이터 사이언티스트", "전략적인 분석과 시스템적 사고로 복잡한 문제 해결에 강해요."),
        ("💻 AI 엔지니어", "미래를 설계하고 기술을 주도하는 리더형 인재예요."),
        ("🏛️ 정책 분석가", "장기적인 계획과 객관적 판단력이
