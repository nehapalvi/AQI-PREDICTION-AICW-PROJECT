# pages/1_About.py

import streamlit as st

st.header("📌 About Project")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/data.png")
    st.markdown("**Data**\n- City AQI dataset\n- Time-based features")

with col2:
    st.image("assets/model.png")
    st.markdown("**Models**\n- XGBoost\n- Random Forest\n- LSTM")

with col3:
    st.image("assets/predict.png")
    st.markdown("**Output**\n- AQI Value\n- Category (Good/Bad)")