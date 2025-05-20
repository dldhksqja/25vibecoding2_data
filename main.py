import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 행정기관별 총 인구수 시각화 (남녀합계.xlsx 기반)")

# 파일 업로드
uploaded_file = st.file_uploader("남녀합계.xlsx 파일을 업로드하세요", type=["xlsx"])

if uploaded_file:
    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(uploaded_file)
        df.columns = df.iloc[2]
        df_clean = df.iloc[3:].copy()

        # 필요한 열 선택
        df_population = df_clean[['행정기관', '총 인구수']].dropna()
        df_population['총 인구수'] = df_population['총 인구수'].str.replace(",", "").astype(int)

        # 시각화
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
        st.success("✅ 시각화 완료!")

    except Exception as e:
        st.error(f"파일 처리 중 오류가 발생했습니다: {e}")
else:
    st.info("📥 좌측에 엑셀 파일을 업로드해 주세요.")
