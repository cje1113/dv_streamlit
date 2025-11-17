import streamlit as st

st.set_page_config(
    page_title="서브페이지",
    page_icon=":smile:",
    layout='centered',
    initial_sidebar_state="collapsed"
)

st.write("서브페이지")
st.write("""
## 주요 기능
- 데이터 시각화
- 대시보드 생성
- 사용자 인터랙션
""")