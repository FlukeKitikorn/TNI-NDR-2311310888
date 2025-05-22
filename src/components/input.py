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
        # options_period = {
        #     0: ("60m", 60),  # 1H
        #     1: ("1d", 30),   # 1D (30 วัน)
        #     2: ("1d", 30),   # 1M (ใช้ daily แล้ว group เป็นเดือน)
        #     3: ("1d", 180),  # 6M (180 วัน)
        # }
        selection = st.segmented_control(
                    "Tool",
                    options=options_period.keys(),
                    format_func=lambda option: options_period[option],
                    selection_mode="single",
                    key="period_select"
                )
        if selection == '60m':
            limit_bar = 48  # 2 วันชั่วโมงละแท่ง
        elif selection == '1d':
            limit_bar = 30  # 30 วัน
        elif selection == '1M':
            limit_bar = 90  # 3 เดือน สำหรับกลุ่มเป็นรายเดือน
        elif selection == '6M':
            limit_bar = 180  # 6 เดือน
        else:
            limit_bar = 30  # default
    
    with col4:
        st.write("") 
    
    '''
    print(json.dumps({
            "choice": choice,
            "indicator": indicator,
            "period": selection,
            "limit": limit_bar
        }, ensure_ascii=False, indent=2))
    '''

    return choice ,indicator, limit_bar, selection if selection is not None else None
