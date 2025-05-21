import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.io import output_file

# ===== Mock Data =====
num_days = 30
dates = [datetime.now() - timedelta(days=i) for i in reversed(range(num_days))]

df = pd.DataFrame({
    "Date": dates,
    "Date_str": [d.strftime("%Y-%m-%d") for d in dates],
    "Open": np.random.uniform(90, 110, num_days),
    "Close": np.random.uniform(90, 110, num_days),
    "High": np.random.uniform(110, 120, num_days),
    "Low": np.random.uniform(80, 90, num_days),
    "Volume": np.random.randint(1000, 10000, num_days),
})

# แก้ไข BarColor ตามว่า Close มากกว่า Open หรือไม่
df["BarColor"] = ["green" if c >= o else "red" for c, o in zip(df["Close"], df["Open"])]

# ตัวอย่าง indicators (SMA 5 และ SMA 10)
df["SMA5"] = df["Close"].rolling(window=5).mean()
df["SMA10"] = df["Close"].rolling(window=10).mean()

# ===== พารามิเตอร์ global =====
close_line = True
include_vol = True
indicators = ["SMA5", "SMA10"]
indicator_colors = {
    "SMA5": "blue",
    "SMA10": "orange",
}

# ===== ฟังก์ชันสร้างกราฟ =====
def create_chart():
    candle = figure(x_axis_type="datetime", height=500,
                    x_range=(df.Date.values[0], df.Date.values[-1]),
                    tooltips=[("Date", "@Date_str"), ("Open", "@Open"),
                              ("High", "@High"), ("Low", "@Low"), ("Close", "@Close")])

    candle.segment("Date", "Low", "Date", "High", color="black", line_width=0.5, source=df)
    candle.segment("Date", "Open", "Date", "Close",
                   line_color="BarColor", line_width=2 if len(df) > 100 else 6, source=df)

    candle.xaxis.axis_label = "Date"
    candle.yaxis.axis_label = "Price ($)"

    if close_line:
        candle.line("Date", "Close", color="black", source=df)

    for indicator in indicators:
        if indicator in df:
            candle.line("Date", indicator, color=indicator_colors.get(indicator, "gray"),
                        line_width=2, source=df, legend_label=indicator)

    volume = None
    if include_vol:
        volume = figure(x_axis_type="datetime", height=150,
                        x_range=(df.Date.values[0], df.Date.values[-1]))
        volume.segment("Date", 0, "Date", "Volume",
                       line_width=2 if len(df) > 100 else 6,
                       line_color="BarColor", alpha=0.8, source=df)
        volume.yaxis.axis_label = "Volume"

    return column(children=[candle, volume], sizing_mode="scale_width") if volume else candle

# ===== เรียกดูผลลัพธ์ผ่าน Browser =====
output_file("candlestick_test.html")
show(create_chart())
