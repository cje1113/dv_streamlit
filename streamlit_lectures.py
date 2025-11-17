import streamlit as st

st.set_page_config(
    page_title="하교수의 Streamlit",
    page_icon="👋",
    layout='wide',

    # 사이드바 초기 상태: auto, collasped, expanded
    initial_sidebar_state='expanded',
    
    # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목
    menu_items={
    'Get help': 'https://docs.streamlit.io',
    'Report a bug': 'https://streamlit.io',
    'About': "### 하정훈 교수 \n - [홍익대학교 산업데이터공학과](https://ie.hongik.ac.kr/ie/0201.do?mode=view&deptCd=AAB530&S1=2006&S2=10077)"
    }
)

"# 환영합니다! 하교수의 Streamlit 앱에 오신 것을 환영합니다."

# 사이드바 설정
st.sidebar.title("다양한 사이드바 위젯들")

st.sidebar.checkbox("외국인 포함")
st.sidebar.checkbox("고령인구 포함")
st.sidebar.divider()    # 구분선
st.sidebar.radio("데이터 타입", ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20, 50))
st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])