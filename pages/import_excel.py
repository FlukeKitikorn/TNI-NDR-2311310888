import streamlit as st
import pandas as pd
from Home import color_bg
from src.controller.loadexcel import excel_to_pandas

st.markdown(
    "<h1 style='text-align: center; color: white;'>Import stock</h1>",
    unsafe_allow_html=True
)
st.markdown(color_bg(), unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    uploaded_file = st.file_uploader("")
    if uploaded_file is not None:
        try:
            excel_to_pandas(uploaded_file)
            # แสดงผลเบื้องต้น
            col3.success("✅ File loaded successfully!")

        except Exception as e:
            st.error(f"❌ Error loading Excel file: {e}")
