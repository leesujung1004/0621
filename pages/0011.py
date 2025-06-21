import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# ----------------- 설정 -----------------
st.set_page_config(page_title="🌍 글로벌 시가총액 TOP10 주식 변화", layout="wide")

st.title("📈 글로벌 시가총액 TOP10 기업의 최근 1년 주가 변화")
st.markdown("데이터 출처: Yahoo Finance")

# ----------------- 시가총액 TOP 10 (2025 기준 추정) -----------------
top10_stocks = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Saudi Aramco (2222.SR)": "2222.SR",
    "Alphabet (GOOGL)": "GOOGL",
    "Amazon (AMZN)": "AMZN",
    "NVIDIA (NVDA)": "NVDA",
    "Berkshire Hathaway (BRK-B)": "BRK-B",
    "Meta (META)": "META",
    "TSMC (TSM)": "TSM",
    "Tesla (TSLA)": "TSLA"
}

# ----------------- 날짜 설정 -----------------
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# ----------------- 데이터 가져오기 -----------------
st.info("🔄 데이터를 불러오는 데 10초 정도 걸릴 수 있어요...")
data = {}
for name, ticker in top10_stocks.items():
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    data[name] = df

# ----------------- 시각화 -----------------
fig = go.Figure()
for name, df in data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["Close"],
        mode='lines',
        name=name
    ))

fig.update_layout(
    title="📊 최근 1년간 글로벌 시가총액 TOP10 기업의 주가 추이",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    templat

