import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 행정기관별 총 인구수 시각화 (남녀합계.xlsx from GitHub)")

# GitHub raw URL
excel_url = "https://raw.githubusercontent.com/dldhksqja/25vibecoding2_data/main/%EB%82%A8%EB%85%80%ED%95%A9%EA%B3%84.xlsx"

try:
    # GitHub에서 엑셀 데이터 불러오기
    df = pd.read_excel(excel_url)
    df.columns = df.iloc[2]  # 3번째 행을 컬럼명으로
    df_clean = df.iloc[3:].copy()  # 4번째 행부터 실제 데이터

    # '행정기관'과 '총 인구수' 컬럼 정제
    df_population = df_clean[['행정기관', '총 인구수']].dropna()
    df_population['총 인구수'] = df_population['총 인구수'].str.replace(",", "").astype(int)

    # Plotly 그래프 생성
    fig = px.bar(
        df_population,
        x='행정기관',
        y='총 인구수',
        title='행정기관별 총 인구수',
        labels={'총 인구수': '총 인구수 (명)', '행정기관': '지역'},
        template='plotly_white'
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"❌ GitHub 파일 처리 중 오류:\n\n{e}")
