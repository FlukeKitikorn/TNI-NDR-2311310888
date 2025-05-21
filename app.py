import streamlit as st
from src.components.header import show_header  
from src.components.input import  search_box
from src.components.content import candle_chart


def main():
    st.sidebar.title("เมนูหลัก")
    menu = st.sidebar.selectbox("เลือกเมนู", ["หน้า UI", "หน้าอื่น"])

    if menu == "หน้า UI":
        show_header()
    else:
        st.write("นี่คือหน้าอื่น")

def color_bg():
    page_bg_color = '''
    <style>
        [data-testid="stAppViewContainer"]{
            background-image: linear-gradient(60deg, #abecd6 0%, #fbed96 100%);
        }
    </style>
    '''
    return page_bg_color

if __name__ == "__main__":

    st.set_page_config(page_title='SWAST - Handover Delays',  layout='wide')
    st.markdown(color_bg(), unsafe_allow_html=True)
    show_header()
    st.divider()
    search_box()
    candle_chart()
    # main()
