import streamlit as st

def search_box():
    col1, col2, col3 = st.columns([1, 1, 3])

    st.header("MALEE : บริษัท มาลีกรุ๊ป จำกัด (มหาชน)")
    with col1:
        types = st.selectbox(
            "Contact Method:",
            ("Email", "Home phone", "Mobile phone"),
            index=None
        )
        # st.write("You selected:", types)

    with col2:
        indicators = st.selectbox(
            "Indicator:",
            ("SMA", "EMA", "MACD"),
            index=None
        )
        # st.write("You selected:", indicators)

    with col3:
        st.write("")  
