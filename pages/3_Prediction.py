import streamlit as st
import numpy as np
from datetime import datetime
from utils.load_models import load_model
from utils.mapping import reverse_city_mapping

st.header("🔮 AQI Prediction")

now = datetime.now()

# ---------------------------
# MODEL SELECT & CITY SELECT
# ---------------------------
col_m, col_c = st.columns(2)
with col_m:
    model_name = st.selectbox("Select Model", ["XGBoost", "LSTM"])
with col_c:
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

c1, c2, c3 = st.columns(3)
with c1:
    PM25    = st.number_input("PM2.5",   value=50.0, key="pm25")
    NOx     = st.number_input("NOx",     value=40.0, key="nox")
    SO2     = st.number_input("SO2",     value=15.0, key="so2")
    Benzene = st.number_input("Benzene", value=5.0,  key="benzene")
with c2:
    PM10    = st.number_input("PM10",    value=80.0, key="pm10")
    NH3     = st.number_input("NH3",     value=10.0, key="nh3")
    O3      = st.number_input("O3",      value=25.0, key="o3")
    Toluene = st.number_input("Toluene", value=10.0, key="toluene")
with c3:
    NO      = st.number_input("NO",      value=20.0, key="no")
    NO2     = st.number_input("NO2",     value=30.0, key="no2")
    CO      = st.number_input("CO",      value=1.0,  key="co")
    Xylene  = st.number_input("Xylene",  value=8.0,  key="xylene")

st.subheader("Enter Date & Time")

d1, d2, d3, d4, d5 = st.columns(5)
with d1:
    Year   = st.number_input("Year",   value=now.year,   key="year")
with d2:
    Month  = st.number_input("Month",  value=now.month,  key="month")
with d3:
    Day    = st.number_input("Day",    value=now.day,    key="day")
with d4:
    Hour   = st.number_input("Hour",   value=now.hour,   key="hour")
with d5:
    Minute = st.number_input("Minute", value=now.minute, key="minute", disabled=disable_minute)

# ---------------------------
# PREDICT BUTTON
# ---------------------------
if st.button("Predict", use_container_width=True):

    model = load_model(model_name)

    # ===========================
    # XGBOOST (WITH SMART LAG)
    # ===========================
    if model_name == "XGBoost":

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
    st.markdown("---")
    out1, out2 = st.columns(2)
    with out1:
        st.success(f"Predicted AQI: {round(pred, 2)}")
    with out2:
        if pred <= 50:
            st.success("Good 😊")
        elif pred <= 100:
            st.info("Moderate 😐")
        elif pred <= 200:
            st.warning("Poor 😷")
        else:
            st.error("Very Unhealthy 🚫")