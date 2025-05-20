import streamlit as st

def show_header():
    st.set_page_config(page_title='SWAST - Handover Delays',  layout='wide', page_icon=':ambulance:')

    #  ------Header------
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image('./src/img/Leaf-Trade.png', width=250)
    with col2:
        st.title("Leaf Trade")
        st.markdown(" **tel:** 01392 451192 **| website:** https://www.swast.nhs.uk **| email:** mailto:data.science@swast.nhs.uk")
    #  ------End Header------

