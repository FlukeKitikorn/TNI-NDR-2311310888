import streamlit as st
from src.controller.loadjson import load_stock_list
import json
import uuid

def search_box():
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])
    stock_list = load_stock_list()

    with col1:   
        options = [f"{stock['symbol']} | {stock['name']}" for stock in stock_list]
        selected_stock = st.selectbox("เลือกหุ้น:", options, index=None, key="stock_select")
        choice = None
        
        if selected_stock:
            choice = selected_stock.split(" | ")[0] 
        # st.write("You selected:", types)
    st.header(selected_stock if selected_stock else "กรุณาเลือกหุ้น")
    with col2:
        indicator = st.multiselect(
            "Indicator:",
            ["SMA5", "SMA10", "EMA", "MACD"],
            key="indicator_select"
        )
        # st.write("You selected:", indicators)

    with col3:
        options_period = {
            '60m': "1H",
            '1d': "1D",
            '1M': "1M",
            '6M': "6M",
        }
        selection = st.segmented_control(
                    "Tool",
                    options=options_period.keys(),
                    format_func=lambda option: options_period[option],
                    selection_mode="single",
                    key="period_select"
                )
    
    with col4:
        st.write("") 
    
    '''
    print(json.dumps({
            "choice": choice,
            "indicator": indicator,
            "period": selection
        }, ensure_ascii=False, indent=2))
    '''

    return choice ,indicator, selection if selection is not None else None
