
import streamlit as st

st.title(" AQI Predictions")
st.markdown("---")

st.subheader("Project Overview")
st.markdown("""
This project focuses on predicting the Air Quality Index (AQI) using advanced machine learning and deep learning techniques. By analyzing historical atmospheric data.

We train and evaluate two primary architectures to find the best approach for time-series forecasting:
* **LSTM (Long Short-Term Memory):** A deep learning recurrent neural network designed to capture sequential patterns over time.
* **XGBoost:** A highly efficient and powerful tree-based gradient boosting framework used for high-performance regression.
""")

st.markdown("---")

st.subheader(" Project Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/data.png", caption="Dataset Visualizations", use_container_width=True)
    st.image("assets/model.png", caption="Model Training & Evaluation", use_container_width=True)

with col2:
    st.image("assets/predict.png", caption="Prediction Results", use_container_width=True)
    
    st.markdown("###  Model Performance Summary")
    st.success("**LSTM Model:** 98% R^2 Score")
    st.warning("**XGBoost Model:** 96% R^2 Score")
    st.info("Both models are logged and tracked using **MLflow** for full reproducibility.")