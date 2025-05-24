import streamlit as st
from src.components.header import show_header
from src.components.input import  search_box
from src.components.content import candle_chart
from Home import color_bg

st.markdown(
    "<h1 style='text-align: center; color: white;'>Search Stocks</h1>",
    unsafe_allow_html=True
)
# st.set_page_config(layout='wide')
st.markdown(color_bg(), unsafe_allow_html=True)
# show_header()
st.divider()
symbol, indicators, limit, period = search_box()
candle_chart(symbol, period, limit, indicators)