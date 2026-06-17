import streamlit as st
import numpy as np
from utils.load_models import load_model
from utils.mapping import reverse_city_mapping

st.header("🔮 AQI Prediction")

# ---------------------------
# MODEL SELECT
# ---------------------------
model_name = st.selectbox("Select Model", ["XGBoost", "Random Forest", "LSTM"])

# ---------------------------
# CITY SELECT
# ---------------------------
city = st.selectbox("Select City", list(reverse_city_mapping.keys()))
city_encoded = reverse_city_mapping[city]

# ---------------------------
# DISABLE LOGIC (IMPORTANT)
# ---------------------------
disable_minute = True if model_name == "LSTM" else False

# ---------------------------
# INPUTS (WITH DEFAULT VALUES)
# ---------------------------
st.subheader("Enter Values")

PM25 = st.number_input("PM2.5", value=50.0, key="pm25")
PM10 = st.number_input("PM10", value=80.0, key="pm10")
NO = st.number_input("NO", value=20.0, key="no")
NO2 = st.number_input("NO2", value=30.0, key="no2")
NOx = st.number_input("NOx", value=40.0, key="nox")
NH3 = st.number_input("NH3", value=10.0, key="nh3")
CO = st.number_input("CO", value=1.0, key="co")
SO2 = st.number_input("SO2", value=15.0, key="so2")
O3 = st.number_input("O3", value=25.0, key="o3")

Benzene = st.number_input("Benzene", value=5.0, key="benzene")
Toluene = st.number_input("Toluene", value=10.0, key="toluene")
Xylene = st.number_input("Xylene", value=8.0, key="xylene")

Year = st.number_input("Year", value=2020, key="year")
Month = st.number_input("Month", value=6, key="month")
Day = st.number_input("Day", value=15, key="day")
Hour = st.number_input("Hour", value=12, key="hour")
Minute = st.number_input("Minute", value=0, key="minute", disabled=disable_minute)

# ---------------------------
# PREDICT BUTTON
# ---------------------------
if st.button("Predict"):

    model = load_model(model_name)

    # ===========================
    # RANDOM FOREST
    # ===========================
    if model_name == "Random Forest":

        features = np.array([[ 
            city_encoded, PM25, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,
            Benzene, Toluene, Xylene,
            Year, Month, Day, Hour, Minute
        ]])

        pred = model.predict(features)[0]

    # ===========================
    # XGBOOST (WITH SMART LAG)
    # ===========================
    elif model_name == "XGBoost":

        st.info("Lag features auto-generated")

        base_aqi = PM25 * 1.2

        aqi_lag1 = base_aqi * 0.9
        aqi_lag2 = base_aqi * 0.8
        aqi_lag3 = base_aqi * 0.7

        aqi_roll3 = (aqi_lag1 + aqi_lag2 + aqi_lag3) / 3
        aqi_roll6 = (aqi_lag1 + aqi_lag2 + aqi_lag3 + base_aqi*0.85 + base_aqi*0.75 + base_aqi) / 6

        features = np.array([[ 
            city_encoded, PM25, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,
            Benzene, Toluene, Xylene,
            Year, Month, Day, Hour, Minute,
            aqi_lag1, aqi_lag2, aqi_lag3, aqi_roll3, aqi_roll6
        ]])

        pred = model.predict(features)[0]

    # ===========================
    # LSTM
    # ===========================
    elif model_name == "LSTM":

        st.info("Using sequence-based input")

        features = np.array([[ 
            city_encoded, PM25, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,
            Benzene, Toluene, Xylene,
            Year, Month, Day, Hour
        ]])

        # reshape for LSTM
        features = features.reshape((1, features.shape[1], 1))

        pred = model.predict(features)[0][0]

    # ---------------------------
    # OUTPUT
    # ---------------------------
    st.success(f"Predicted AQI: {round(pred,2)}")

    if pred <= 50:
        st.success("Good 😊")
    elif pred <= 100:
        st.info("Moderate 😐")
    elif pred <= 200:
        st.warning("Poor 😷")
    else:
        st.error("Very Unhealthy 🚫")