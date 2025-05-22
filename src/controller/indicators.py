import plotly.graph_objects as go

def add_indicator(fig, df, indicator, color="black"):
    if indicator == "EMA":
        df["EMA12"] = df["close"].ewm(span=12, adjust=False).mean()
        df["EMA26"] = df["close"].ewm(span=26, adjust=False).mean()
        
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["EMA12"],
            line=dict(color="red", width=1),
            name="EMA12"
        ))
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["EMA26"],
            line=dict(color="blue", width=1),
            name="EMA26"
        ))

    elif indicator == "SMA5":
        df["SMA5"] = df["close"].rolling(window=5).mean()
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["SMA5"],
            line=dict(color=color, width=1),
            name="SMA5"
        ))

    elif indicator == "SMA10":
        df["SMA10"] = df["close"].rolling(window=10).mean()
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["SMA10"],
            line=dict(color=color, width=1),
            name="SMA10"
        ))

    elif indicator == "MACD":
        ema12 = df["close"].ewm(span=12, adjust=False).mean()
        ema26 = df["close"].ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        df["MACD"] = macd
        df["Signal"] = signal
        df["Histogram"] = histogram

        # เส้น MACD
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["MACD"],
            line=dict(color=color, width=1),
            name="MACD"
        ))

        # เส้น Signal
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["Signal"],
            line=dict(color="grey", width=1, dash='dot'),
            name="Signal"
        ))

        # Histogram (แท่งขึ้นลง)
        fig.add_trace(go.Bar(
            x=df["date"], y=df["Histogram"],
            name="MACD Histogram",
            marker_color=["green" if v >= 0 else "red" for v in df["Histogram"]],
            opacity=0.3,
            showlegend=False
        ))
