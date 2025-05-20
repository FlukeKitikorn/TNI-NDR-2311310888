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

if __name__ == "__main__":
    show_header()
    st.divider()
    search_box()
    candle_chart()
    # main()
