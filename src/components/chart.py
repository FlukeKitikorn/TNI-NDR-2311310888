import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
    if data is None or "time" not in data:
        return

    df = pd.DataFrame({
        "date": pd.to_datetime(data["time"], unit='s'),
        "open": data["open"],
        "high": data["high"],
        "low": data["low"],
        "close": data["close"],
        "volume": data["volume"],
    })

    # subplot: 2 rows (candlestick + volume), shared x-axis
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.05,
                        row_heights=[0.7, 0.3],
                        subplot_titles=("Candlestick", "Volume"))

    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='green',
        decreasing_line_color='red',
        name="Price"
    ), row=1, col=1)

    # Volume chart (bar)
    fig.add_trace(go.Bar(
        x=df['date'],
        y=df['volume'],
        marker_color='lightblue',
        name="Volume"
    ), row=2, col=1)

    tickformat = time_xaxis(data.get("period", "1d"))

    fig.update_layout(
        xaxis=dict(tickformat=tickformat,
                    rangeslider=dict(visible=False),  # ✅ ปิด rangeslider
                    automargin=True),
        xaxis2=dict(tickformat=tickformat,
                    automargin=True),
        height=500,
        template="plotly_white",
        showlegend=False,
        margin=dict(t=30, b=30, l=50, r=30)
    )

    st.plotly_chart(fig, use_container_width=True)
