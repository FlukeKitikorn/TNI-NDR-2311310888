from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
from config import API_ID, API_KEY

# ===== connect part =====
def get_connect():
    try:
        investor = Investor(
            app_id=API_ID,
            app_secret=API_KEY,
            broker_id="SANDBOX",
            app_code="SANDBOX",
            is_auto_queue=False
        )
        return investor.Equity(account_no="kiti-E")
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
            broker_id="SANDBOX",
            app_code="SANDBOX",
            is_auto_queue=False
        )
        return investor.MarketData()
    except SettradeError as e:
        print("---- error message ----")
        print(e)
        return None
# ===== End  fetch market data =====

# ===== fetch candlestick data =====
def get_candlestick(symbol, interval="1d", limit=30, start=None, end=None, normalized=False):
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

# ===== example usage =====
if __name__ == "__main__":
    import json
    result = get_candlestick("PTT", interval="1d", limit=5)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("No data returned.")
