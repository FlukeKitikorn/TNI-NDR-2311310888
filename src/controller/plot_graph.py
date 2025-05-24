import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib

matplotlib.rcParams['font.family'] = 'DejaVu Sans'

def plot_price_trend(df, title="Closing Price Trend"):
    """
    ฟังก์ชันนี้รับ DataFrame ที่มีคอลัมน์ 'วันที่' และ 'ราคาปิด'
    แล้วพล็อตกราฟราคาปิดพร้อมแนวโน้ม Linear Regression
    """
    df_sorted = df.sort_values("วันที่")

    X = df_sorted["วันที่"].map(pd.Timestamp.toordinal).values.reshape(-1, 1)
    y = df_sorted["ราคาปิด"].values

    model = LinearRegression()
    model.fit(X, y)
    trend = model.predict(X)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_sorted["วันที่"], y, label="Actual Closing Price")
    ax.plot(df_sorted["วันที่"], trend, label="Trend (Linear Regression)", linestyle="--", color="red")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price (Baht)")
    ax.legend()
    ax.grid(True)
    plt.title("Closing Price Trend")
    plt.tight_layout()

    return fig
