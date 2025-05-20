import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(layout="wide")

# 샘플 화재 발생 데이터
fire_data = pd.DataFrame({
    'latitude': [34.0522, 36.7783, 40.7128],
    'longitude': [-118.2437, -119.4179, -74.0060],
    'location': ['Los Angeles, CA', 'Central California', 'New York City, NY'],
    'description': ['Wildfire near LA', 'Forest fire in Central CA', 'Building fire in NYC']
})

st.title("🔥 미국 화재 발생 지역 지도 시각화")
st.markdown("간단한 마커 기반 지도 시각화 예시입니다.")

# 지도 생성
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
marker_cluster = MarkerCluster().add_to(m)

# 마커 추가
for _, row in fire_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        tooltip=row['location'],
        popup=f"<b>{row['location']}</b><br>{row['description']}"
    ).add_to(marker_cluster)

# 지도 출력
st_data = st_folium(m, width=900, height=600)
