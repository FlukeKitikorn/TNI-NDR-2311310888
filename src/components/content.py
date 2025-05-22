import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import json
from src.components.chart import chart
from Datahandle.settrade.data import get_candlestick

def candle_chart(symbol, period, limit, indicators):
    col1, col2 = st.columns([2.5,1])
    data = np.random.randn(10, 1)
    result = get_candlestick(symbol, interval=period, limit=limit)
    # print(json.dumps(result, indent=4))

    with col1:
        chart(result, indicators)

    with col2:
        st.write(data)  