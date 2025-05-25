import streamlit as st
from src.controller.loadjson import load_stock_list
import json
import uuid

def search_box():
    col1, col2, col3, col4 = st.columns([1, 1, 2, 1.5])
    stock_list = load_stock_list()

    with col1:   
        options = [f"{stock['symbol']} | {stock['name']}" for stock in stock_list]
        selected_stock = st.selectbox("Select stock", options, index=None, key="stock_select")
        choice = None
        
        if selected_stock:
            choice = selected_stock.split(" | ")[0] 
            
    st.header(selected_stock if selected_stock else "Please select stock")
    with col2:
        indicator = st.multiselect(
            "Indicator",
            ["SMA5", "SMA10", "EMA", "MACD"],
            key="indicator_select"
        )

    with col3:
        options_period = {
            '5m': "1 Min",
            '60m': "1 Hour",
            '1d': "1 Day",
            '1M': "1 Month",
        }
        selection = st.segmented_control(
                    "Candlestick Interval",
                    options=options_period.keys(),
                    format_func=lambda option: options_period[option],
                    selection_mode="single",
                    key="period_select"
                )
        limit_bar = 30 # default
        if selection == '5m':
            limit_bar = 288  # 24 ชม. (12 แท่ง/ชม. × 24 ชม.) = 1 วัน
        elif selection == '60m':
            limit_bar = 168  # 1 สัปดาห์ (24 ชม. × 7 วัน)
        elif selection == '1d':
            limit_bar = 60  # 3 เดือน (20 วันทำการ/เดือน × 3)
        elif selection == '1M':
            limit_bar = 24  # 2 ปี (24 เดือน)
    
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
