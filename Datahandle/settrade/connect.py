from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
from config import API_ID, API_KEY
import json

def get_connect():
    try:
        investor = Investor(
                    app_id=f"{API_ID}",                                 
                    app_secret=f"{API_KEY}", 
                    broker_id="SANDBOX",
                    app_code="SANDBOX",
                    is_auto_queue = False)

        return investor.Equity(account_no="kiti-E")  

    # ------check account info------ 
        # account_info = deri.get_account_info()
        # print(json.dumps(account_info, indent=4))
    except SettradeError as e:
        print("---- error message  ----")
        print(e)
        print("---- error code ----")
        print(e.code)
        print("---- status code ----")
        print(e.status_code)
        return None
    
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