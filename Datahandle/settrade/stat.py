import pandas as pd
from datetime import datetime

def summarize_stock_data(data):
    if data is None:
        return None
    
    df = pd.DataFrame(data)
    if df.empty:
        return None

    highest_high = df['high'].max()
    lowest_low = df['low'].min()
    average_close = df['close'].mean()
    total_volume = df['volume'].sum()

    # ราคาล่าสุด
    last_close = df['close'].iloc[-1]
    # ราคาก่อนล่าสุด
    previous_close = df['close'].iloc[-2] if len(df['close']) > 1 else None
    # อัตราการเปลี่ยนแปลง
    if previous_close is not None and previous_close != 0:
        change = last_close - previous_close
        percent_change = (change / previous_close) * 100
    else:
        change = None
        percent_change = None


    return highest_high, lowest_low, average_close, total_volume, change, percent_change, last_close
