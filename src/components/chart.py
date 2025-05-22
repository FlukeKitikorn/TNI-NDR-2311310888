import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.controller.indicators import add_indicator


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

def chart(data, indicator=None):
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
    # เพิ่มคอลัมน์ color สำหรับ volume bar
    df['color'] = np.where(df['close'] >= df['open'], 'green', 'red')

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
        marker_color=df['color'],
        name="Volume"
    ), row=2, col=1)

    indicator_colors = {
        "SMA5": "royalblue",
        "SMA10": "darkorange",
        "EMA": "mediumvioletred",
        "MACD": "seagreen"
    }

    legend_texts = []
    for tool in indicator:
        color = indicator_colors.get(tool.upper(), "black")
        add_indicator(fig, df, tool, color=color)
        if tool == "EMA":
            legend_texts.append(f'<span style="color: red">EMA12</span>')
            legend_texts.append(f'<span style="color: blue">EMA26</span>')
        else:
            legend_texts.append(f'<span style="color:{color}">{tool}</span>')

    # สร้าง annotation แสดง legend บอกชื่อและสี
    fig.add_annotation(
        xref="paper", yref="paper",
        x=0.99, y=0.94,  
        showarrow=False,
        align="left",
        bgcolor="rgba(255,255,255,0.9)",  # เพิ่มความทึบให้มองเห็นชัด
        bordercolor="black",
        borderwidth=1,
        borderpad=6,  #ขยาย padding ให้กล่องใหญ่ขึ้น
        text="Indicators:<br>" + "<br>".join(legend_texts),
        font=dict(size=13)  
    )


    for tool in indicator:
        add_indicator(fig, df, tool)


    # 1d for default
    tickformat = time_xaxis(data.get("period", "1d")) 

    fig.update_layout(
        xaxis=dict(tickformat=tickformat,
                    rangeslider=dict(visible=False),  # ✅ ปิด rangeslider
                    automargin=True),
        xaxis2=dict(tickformat=tickformat,
                    automargin=True),
        height=550,
        template="plotly_white",
        showlegend=False,
        margin=dict(t=30, b=30, l=50, r=30)
    )

    st.plotly_chart(fig, use_container_width=True)
