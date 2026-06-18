import streamlit as st

st.title("AQI Prediction System")
st.markdown("---")

st.subheader("Project Overview")
st.markdown("""
Air quality has become one of the most critical environmental concerns, especially in rapidly urbanizing countries like India. 
This project focuses on predicting the **Air Quality Index (AQI)** across **26 major Indian cities** using advanced machine learning techniques.

We analyze historical atmospheric pollutant data — including PM2.5, PM10, NO2, CO, SO2, O3, and more — to build a robust 
forecasting system that can predict AQI levels with high accuracy.

Our model is trained on real-world data and incorporates **time-based lag features** and **rolling averages** to capture 
temporal patterns in air pollution.
""")

st.markdown("---")

st.subheader("Model Architecture")
st.markdown("""
We use **XGBoost (Extreme Gradient Boosting)** — a highly efficient tree-based ensemble learning algorithm — as our 
primary prediction model.

**Why XGBoost?**
- Handles large datasets with high-dimensional features efficiently
- Naturally captures non-linear relationships between pollutants and AQI
- Supports custom lag and rolling window features for time-series forecasting
- Robust to missing values and outliers in real-world sensor data
- Faster training compared to deep learning models with comparable accuracy
""")

st.markdown("---")

st.subheader("Dataset")
st.markdown("""
- **Cities covered:** 26 major Indian cities including Delhi, Mumbai, Chennai, Bengaluru, and more
- **Features:** PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene
- **Engineered features:** AQI lag values (lag1, lag2, lag3) and rolling averages (roll3, roll6)
- **Time range:** Multi-year hourly data for robust temporal modeling
""")

st.markdown("---")

st.subheader("Project Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/data.png", caption="Dataset Visualizations", use_container_width=True)
    st.image("assets/model.png", caption="Model Training & Evaluation", use_container_width=True)

with col2:
    st.image("assets/predict.png", caption="Prediction Results", use_container_width=True)

    st.markdown("---")
    st.markdown("### 🏆 Model Performance")
    st.success("**XGBoost** — R² Score: **96%**")
    st.info("**RMSE:** Low error margin across all 26 cities")
    st.info("**MAE:** Consistent performance on unseen test data")

st.markdown("---")

