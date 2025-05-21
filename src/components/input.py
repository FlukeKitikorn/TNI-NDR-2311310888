import streamlit as st
from src.controller.loadjson import load_stock_list

def search_box():
    col1, col2, col3 = st.columns([1, 1, 3])

    # st.header("MALEE : บริษัท มาลีกรุ๊ป จำกัด (มหาชน)")
    with col1:
        stock_list = load_stock_list()
        options = [f"{stock['symbol']} | {stock['name']}" for stock in stock_list]
        selected_stock = st.selectbox("เลือกหุ้น:", options, index=None)
        if selected_stock:
            st.write(f"คุณเลือก: {selected_stock}")
        # st.write("You selected:", types)

    with col2:
        indicators = st.selectbox(
            "Indicator:",
            ("SMA", "EMA", "MACD"),
            index=None
        )
        # st.write("You selected:", indicators)

    with col3:
        st.write("")  
