'''
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource

# ===== Mock Data =====
num_days = 180  # รองรับหลายช่วงเวลา
dates = [datetime.now() - timedelta(days=i) for i in reversed(range(num_days))]

df = pd.DataFrame({
    "Date": dates,
    "Open": np.random.uniform(90, 110, num_days),
    "Close": np.random.uniform(90, 110, num_days),
    "High": np.random.uniform(110, 120, num_days),
    "Low": np.random.uniform(80, 90, num_days),
    "Volume": np.random.randint(1000, 10000, num_days),
})
df["Date_str"] = df["Date"].dt.strftime("%Y-%m-%d")
df["BarColor"] = ["green" if c >= o else "red" for c, o in zip(df["Close"], df["Open"])]
df["SMA5"] = df["Close"].rolling(window=5).mean()
df["SMA10"] = df["Close"].rolling(window=10).mean()

# ===== ฟังก์ชันสำหรับ group เป็นเดือน =====
def group_by_month(df):
    df = df.copy()
    df['YearMonth'] = df['Date'].dt.to_period('M')
    grouped = df.groupby('YearMonth').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    }).reset_index()
    grouped['Date'] = grouped['YearMonth'].dt.to_timestamp()
    grouped["Date_str"] = grouped["Date"].dt.strftime("%b %Y")
    grouped["BarColor"] = ["green" if c >= o else "red" for c, o in zip(grouped["Close"], grouped["Open"])]
    return grouped.drop(columns="YearMonth")

# ===== ฟังก์ชันสร้างกราฟ Bokeh =====
def create_chart(df, indicators=["SMA5", "SMA10"], include_vol=True):
    source = ColumnDataSource(df)

    candle = figure(x_axis_type="datetime", height=500, title="กราฟหุ้น",
                    x_range=(df["Date"].iloc[0], df["Date"].iloc[-1]),
                    tooltips=[("Date", "@Date_str"), ("Open", "@Open"),
                              ("High", "@High"), ("Low", "@Low"), ("Close", "@Close")])

    candle.segment("Date", "Low", "Date", "High", color="black", line_width=0.5, source=source)
    candle.segment("Date", "Open", "Date", "Close",
                   line_color="BarColor", line_width=2 if len(df) > 100 else 6, source=source)

    candle.xaxis.axis_label = "Date"
    candle.yaxis.axis_label = "Price"

    for indicator in indicators:
        if indicator in df:
            candle.line("Date", indicator, line_width=2, color="blue", legend_label=indicator, source=source)

    volume_chart = None
    if include_vol:
        volume_chart = figure(x_axis_type="datetime", height=150,
                              x_range=(df["Date"].iloc[0], df["Date"].iloc[-1]))
        volume_chart.segment("Date", 0, "Date", "Volume",
                             line_color="BarColor", line_width=4, alpha=0.6, source=source)
        volume_chart.yaxis.axis_label = "Volume"

    return column(children=[candle, volume_chart], sizing_mode="scale_width") if include_vol else candle

# ===== Streamlit App =====
st.set_page_config(layout="wide")
st.title("📈 Candlestick Chart Viewer")

period_option = st.selectbox("เลือกช่วงเวลา", ["1D", "1M", "6M"])

# เลือกช่วงข้อมูลตามช่วงเวลา
if period_option == "1D":
    df_show = df.tail(30)
elif period_option == "1M":
    df_show = df.tail(60)
    df_show = group_by_month(df_show)
elif period_option == "6M":
    df_show = df
    df_show = group_by_month(df_show)
else:
    df_show = df

# วาดกราฟ
chart = create_chart(df_show)
st.bokeh_chart(chart, use_container_width=True)
'''

import pandas as pd


def chart():
    df = pd.DataFrame(MSFT)[60:120]
    df["date"] = pd.to_datetime(df["date"])

    inc = df.close > df.open
    dec = df.open > df.close

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(tools=TOOLS, width=1000, height=400,
            title="MSFT Candlestick without missing dates",
            background_fill_color="#efefef")
    p.xaxis.major_label_orientation = 0.8 # radians
    p.x_range.range_padding = 0.05

    # map dataframe indices to date strings and use as label overrides
    p.xaxis.major_label_overrides = {
        i: date.strftime('%b %d') for i, date in zip(df.index, df["date"])
    }

    # one tick per week (5 weekdays)
    p.xaxis.ticker = list(range(df.index[0], df.index[-1], 5))

    p.segment(df.index, df.high, df.index, df.low, color="black")

    p.vbar(df.index[dec], 0.6, df.open[dec], df.close[dec], color="#eb3c40")
    p.vbar(df.index[inc], 0.6, df.open[inc], df.close[inc], fill_color="white",
        line_color="#49a3a3", line_width=2)
    return show(p)