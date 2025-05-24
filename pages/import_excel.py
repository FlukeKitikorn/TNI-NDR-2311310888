import streamlit as st
import pandas as pd
from Home import color_bg
from src.controller.loadexcel import excel_to_pandas
from src.controller.plot_graph import plot_price_trend

st.markdown(
    "<h1 style='text-align: center; color: white;'>Import stock</h1>",
    unsafe_allow_html=True
)
st.markdown(color_bg(), unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    uploaded_file = st.file_uploader("", type=["xlsx", "xls"])
    if uploaded_file is not None:
        try:
            data_clean = excel_to_pandas(uploaded_file)
            # แสดงผลเบื้องต้น
            if data_clean.empty:
                st.error("Data is empty after cleaning. Please check your input file.")
            else:
                fig = plot_price_trend(data_clean, title="KBANK Closing Price Trend")
                st.pyplot(fig)
        except Exception as e:
            st.error(f"❌ Error loading Excel file: {e}")

