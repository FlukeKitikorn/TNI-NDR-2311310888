import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go


def time_xaxis(period):
    if period == "1m":
        tickformat = "%d %b %H:%M"   # วันที่ เดือน ชั่วโมง:นาที
    elif period == "1h":
        tickformat = "%d %b %H:%M"   # วันที่ เดือน ชั่วโมง:นาที
    elif period == "1d":
        tickformat = "%d %b"         # วันที่ เดือน
    elif period == "1M":
        tickformat = "%b %Y"         # เดือน ปี
    else:
        tickformat = "%d %b"         # fallback/default
    return tickformat

def chart(data):
    # Mock data สำหรับหุ้น
    np.random.seed(42)
    dates = pd.date_range(end=datetime.today(), periods=100)
    
    # --------- Hold display ---------
    if data is None or "time" not in data:
        return 0

    df = pd.DataFrame({
        "date": pd.to_datetime(data["time"], unit='s'),
        "open": data["open"],
        "high": data["high"],
        "low": data["low"],
        "close": data["close"],
        "volume": data["volume"],
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

    # ---------- change by date ----------
    timeformat = time_xaxis(data["time"])

    fig.update_layout(
        title="",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False,
        xaxis=dict(
            rangeslider_visible=False,
            automargin=True
        ),
        template="plotly_white",
        height=500
    )

    # แสดงผลใน Streamlit
    # st.set_page_config(layout="wide")
    # st.title("📊 Candlestick Chart without Bokeh")
    st.plotly_chart(fig, use_container_width=True)