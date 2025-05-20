import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def candle_chart():
    col1, col2 = st.columns([2.5,1])
    data = np.random.randn(10, 1)

    with col1:
        arr = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
        st.pyplot(fig)
    with col2:
        st.write(data)  