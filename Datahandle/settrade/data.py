import streamlit as st

from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
from config import API_ID, API_KEY, ACC_NO, BORKER_ID, APP_CODE

API_ID = st.secrets["API_ID"]
API_KEY = st.secrets["API_KEY"]
ACC_NO = st.secrets["ACC_NO"]
BORKER_ID = st.secrets["BORKER_ID"]
APP_CODE = st.secrets["APP_CODE"]

# ===== connect part =====
def get_connect():
    try:
        investor = Investor(
            app_id=API_ID,
            app_secret=API_KEY,
            broker_id=BORKER_ID,
            app_code=APP_CODE,
            is_auto_queue=False
        )
        return investor.Equity(account_no=ACC_NO)
    except SettradeError as e:
        print("---- error message ----")
        print(e)
        return None
# ===== End connect part =====

# ===== fetch market data =====
def get_market():
    try:
        investor = Investor(
            app_id=API_ID,
            app_secret=API_KEY,
            broker_id=BORKER_ID,
            app_code=APP_CODE,
            is_auto_queue=False
        )
        return investor.MarketData()
    except SettradeError as e:
        print("---- error message ----")
        print(e)
        return None
# ===== End  fetch market data =====

# ===== fetch candlestick data =====
def get_candlestick(symbol, interval, limit, start=None, end=None, normalized=True):
    market = get_market()
    if not market:
        return None

    try:
        candles = market.get_candlestick(
            symbol=symbol,
            interval=interval,
            limit=limit,
            start=start,
            end=end,
            normalized=normalized
        )
        return candles
    except Exception as e:
        print(f"Can't fetch data of {symbol} [{e}]")
        return None
# ===== End fetch candlestick data =====    
