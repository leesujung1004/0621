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
    "INTJ 🧠": ("📊 데이터 사이언티스트", "논리적이고 전략적인 성향을 살려 복잡한 문제를 분석하는 데 강점이 있어요."),
    "INTP 🔬": ("🧪 연구원", "아이디어가 넘치고 창의적이라 과학, 철학, 수학 등 탐구 중심 분야에 잘 맞아요."),
    "ENTJ 🦸": ("💼 CEO / 기획자", "리더십과 추진력이 강하고 큰 그림을 보는 데 능해요."),
    "ENTP 🎭": ("🎬 콘텐츠 크리에이터", "변화를 좋아하고 재치가 넘쳐 새로운 아이디어에 도전하는 걸 즐겨요."),
    "INFJ 🌌": ("📖 작가 / 상담사", "깊은 통찰력과 타인을 돕는 따뜻한 마음이 있어요."),
    "INFP 🎨": ("🎨 일러스트레이터 / 시나리오 작가", "상상력이 풍부하고 감성이 풍부해서 예술계에 적합해요."),
    "ENFJ 🤝": ("👩‍🏫 교사 / 인사담당자", "사람들과 잘 어울리고 리더십이 있어서 교육, HR 분야에 잘 맞아요."),
    "ENFP 🌈": ("🎤 방송인 / 마케터", "열정이 넘치고 자유로운 영혼이라 대중과 소통하는 분야에 잘 어울려요."),
    "ISTJ 📚": ("🧾 회계사 / 공무원", "신중하고 체계적인 성격으로 규칙이 있는 일을 잘해요."),
    "ISFJ 🧸": ("🩺 간호사 / 사회복지사", "헌신적이고 책임감이 강해 타인을 돌보는 직업에 적합해요."),
    "ESTJ 🧱": ("🏛️ 행정관리자 / 경찰", "현실적이고 조직적인 업무에 강해 리더 역할을 잘 해요."),
    "ESFJ 🎀": ("🧑‍🍳 호텔리어 / 고객상담", "사교성이 뛰어나고 친절해서 서비스직에 잘 어울려요."),
    "ISTP 🛠️": ("🔧 엔지니어 / 정비사", "문제 해결 능력이 뛰어나고 손재주가 좋아요."),
    "ISFP 🌿": ("📷 사진작가 / 플로리스트", "감성이 풍부하고 조용한 예술가 기질을 가졌어요."),
    "ESTP 🚀": ("💰 세일즈 / 창업가", "도전적이고 에너지가 넘쳐 현장 경험 중심의 직업에 적합해요."),
    "ESFP 🎉": ("🎤 MC / 이벤트 플래너", "활발하고 외향적이라 사람 많은 곳에서 빛나요!"),
}

# ------------------ 결과 출력 ------------------
if selected_mbti:
    job, desc = job_recommendations[selected_mbti]
    st.markdown(f"""
    <div style="text-align:center; background-color:#fbeaff; padding:30px; border-radius:20px; box-shadow: 0 0 10px #ffb3ff;">
        <h2 style="color:#ff66c4;">🌟 {selected_mbti} 추천 직업 🌟</h2>
        <h1 style="color:#cc00cc;">{job}</h1>
        <p style="font-size:18px;">💬 {desc}</p>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

# ------------------ 푸터 ------------------
st.divider()
st.markdown("<p style='text-align:center;'>👩‍💻 Made with ❤️ by 진로상담봇 • MBTI Career Recommender</p>", unsafe_allow_html=True)
