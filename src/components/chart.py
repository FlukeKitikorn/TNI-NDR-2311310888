import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

def chart():
    # Mock data สำหรับหุ้น
    np.random.seed(42)
    dates = pd.date_range(end=datetime.today(), periods=100)

    df = pd.DataFrame({
        "date": dates,
        "open": np.random.uniform(100, 110, len(dates)),
        "high": np.random.uniform(110, 115, len(dates)),
        "low": np.random.uniform(95, 100, len(dates)),
        "close": np.random.uniform(100, 110, len(dates)),
    })

    # สร้างกราฟ Candlestick ด้วย Plotly
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='green',
        decreasing_line_color='red'
    )])

    fig.update_layout(
        title="📈 MSFT Candlestick Chart (Plotly)",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False,
        template="plotly_white",
        height=600
    )

    # แสดงผลใน Streamlit
    # st.set_page_config(layout="wide")
    # st.title("📊 Candlestick Chart without Bokeh")
    st.plotly_chart(fig, use_container_width=True)