import streamlit as st
import json
from src.components.header import show_header  
from src.components.input import  search_box
from src.components.content import candle_chart
from Datahandle.settrade.data import get_candlestick
from src.components.chart import chart
from PIL import Image
# from Datahandle.settrade.config import API_ID, API_KEY, ACC_NO, BORKER_ID, APP_CODE

# Define load_image function
def load_image(path):
    return Image.open(path)

#  -------- dump to check ----------
def show_data_from_api(symbol, period, limit):
    result = get_candlestick(symbol, interval=period, limit=limit)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("No data returned.")

def color_bg():
    page_bg_color = '''
    <style>
        [data-testid="stAppViewContainer"]{
            background-image: linear-gradient(60deg, #abecd6 0%, #fbed96 100%);
        }
    </style>
    '''
    return page_bg_color

if __name__ == "__main__":
    # logo = load_image("./src/img/Leaf-Trade.png")
    st.set_page_config(page_title='Leaf Trade',  layout='wide')
    # st.sidebar.image(logo, use_column_width=True)
    show_header()
    st.markdown(color_bg(), unsafe_allow_html=True)
    st.divider()
    symbol, indicators, limit, period = search_box()
    candle_chart(symbol, period, limit, indicators)
    
    # show_data_from_api(symbol, period, limit)
    # main()
