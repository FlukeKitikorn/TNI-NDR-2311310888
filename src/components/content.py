import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import json
from src.components.chart import chart
from Datahandle.settrade.data import get_candlestick
from Datahandle.settrade.stat import summarize_stock_data

def candle_chart(symbol, period, limit, indicators):
    col1, col2 = st.columns([3,1])
    result = get_candlestick(symbol, interval=period, limit=limit)
    # print(json.dumps(result, indent=4))

    if result is None:
        # st.error("Failed to fetch candlestick data.")
        return

    stat = summarize_stock_data(result)
    
    # print(json.dumps(stat))
    highest, lowest, average, total_vol, change, percent_change, last = stat

    with col1:
        chart(result, indicators)
        
    with col2:
        # st.write(data)  
        # st.write(data)
        
        # st.markdown("### ℹ️ Stock Info")
        # st.markdown(f"""
        # **🔹 Symbol**: `{symbol}`  
        # **🔹 Interval**: `{period}`  
        # **🔹 Date Range**: `{start}` ➝ `{end}`  
        # **🔹 Bars Fetched**: `{len(limit)}`  
        # """)

        # st.divider()

        # st.metric("✅ Average Close", f"{avg_close:.2f}")
        # st.metric("📈 Highest High", f"{max_price:.2f}", help=f"on {max_time}")
        # st.metric("📉 Lowest Low", f"{min_price:.2f}", help=f"on {min_time}")
        # st.metric("📦 Total Volume", f"{total_volume:,.0f}")
        if change is not None and percent_change is not None:
            st.metric(label="Change", value=f"{change:+.2f} ({percent_change:+.2f}%)", delta=percent_change)
        else:
            st.metric(label="Change", value="No data")
        st.metric("Highest High", f"{highest:.2f} ฿", border=True)
        st.metric("Lowest Low", f"{lowest:.2f} ฿", border=True)
        st.metric("Total Volume", f"{total_vol:,.2f} ฿", border=True)

        