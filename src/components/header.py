import streamlit as st

def show_header():

    #  ------Header------
    col1, col2, col3 = st.columns([1, 2, 1], vertical_alignment="center")

    with col1:
        st.image('./src/img/Leaf-Trade.png', width=250)
    with col2:
        st.title("Leaf Trade")
        st.markdown(" **tel:** xxx-xxx-xxxx **| website:** https://github.com/FlukeKitikorn/TNI-NDR-2311310888 **| email:** kh.kitikorn_st@tni.ac.th")
    #  ------End Header------

