import streamlit as st
import folium
from streamlit_folium import st_folium

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
folium.Marker([37.5665, 126.9780], tooltip="서울시청").add_to(m)

# 지도 표시
st_data = st_folium(m, width=700, height=500)
