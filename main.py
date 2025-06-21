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
        ("📊 데이터 사이언티스트", "전략적인 사고로 문제 해결을 잘해요."),
        ("💻 인공지능 개발자", "미래 지향적이고 분석적이에요."),
        ("📈 전략 기획자", "계획 수립과 실행에 능숙해요.")
    ],
    "INTP 🔬": [
        ("🧪 연구원", "창의적이고 지식 탐구를 즐겨요."),
        ("👨‍💻 시스템 프로그래머", "논리적 사고가 뛰어나요."),
        ("📚 철학자", "깊은 사고와 이론에 몰입해요.")
    ],
    "ENTJ 🦸": [
        ("💼 CEO / 기획자", "리더십이 강하고 추진력이 뛰어나요."),
        ("📊 경영 컨설턴트", "문제를 빠르게 파악하고
