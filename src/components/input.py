import streamlit as st
from src.controller.loadjson import load_stock_list

def search_box():
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    stock_list = load_stock_list()
    
    with col1:    
        options = [f"{stock['symbol']} | {stock['name']}" for stock in stock_list]
        selected_stock = st.selectbox("เลือกหุ้น:", options, index=None)
        if selected_stock:
            choice = selected_stock
        # st.write("You selected:", types)
    st.header(selected_stock if selected_stock else "กรุณาเลือกหุ้น")
    with col2:
        indicators = st.multiselect(
            "Indicator:",
            ["SMA5", "SMA10", "EMA", "MACD"]
        )
        # st.write("You selected:", indicators)

    with col3:
        options_period = {
            0: "1H",
            1: "1D",
            2: "1M",
            3: "6M",
        }
        selection = st.segmented_control(
                    "Tool",
                    options=options_period.keys(),
                    format_func=lambda option: options_period[option],
                    selection_mode="single",
                )
    
    with col4:
        st.write("")  
