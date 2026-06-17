# pages/2_Dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from utils.mapping import reverse_city_mapping

st.header("📊 AQI Dashboard")

# ---------------------------
# LOAD DATA
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "eda_dataset.csv")

df = pd.read_csv(file_path)

# ---------------------------
# DROPDOWNS
# ---------------------------
city = st.selectbox("Select City", list(reverse_city_mapping.keys()))

# ---------------------------
# FILTER DATA
# ---------------------------
city_encoded = reverse_city_mapping[city]
filtered_df = df[df['City'] == city_encoded]

# ---------------------------
# CHECK DATA
# ---------------------------
if filtered_df.empty:
    st.error("No data available for selected city")
else:
    st.success(f"Showing AQI insights for {city}")

    # ===========================
    # GRAPH 1: AQI TREND
    # ===========================
    st.subheader("📈 AQI Trend Over Time")

    st.markdown("""
    👉 This graph shows how AQI changes over time in the selected city.  
    👉 Helps identify pollution spikes and overall trend (increasing/decreasing).
    """)

    fig1, ax1 = plt.subplots()
    ax1.plot(filtered_df['AQI'])
    ax1.set_title("AQI Trend")
    ax1.set_xlabel("Time Index")
    ax1.set_ylabel("AQI")
    st.pyplot(fig1)

    # ===========================
    # GRAPH 2: PM2.5 vs AQI
    # ===========================
    st.subheader("🌫 PM2.5 vs AQI Relationship")

    st.markdown("""
    👉 This scatter plot shows relationship between PM2.5 and AQI.  
    👉 Higher PM2.5 usually leads to higher AQI (bad air quality).
    """)

    fig2, ax2 = plt.subplots()
    ax2.scatter(filtered_df['PM2.5'], filtered_df['AQI'])
    ax2.set_xlabel("PM2.5")
    ax2.set_ylabel("AQI")
    ax2.set_title("PM2.5 vs AQI")
    st.pyplot(fig2)

    # ===========================
    # GRAPH 3: MONTHLY TREND
    # ===========================
    st.subheader("📅 Monthly Average AQI")

    st.markdown("""
    👉 Shows average AQI for each month.  
    👉 Helps identify seasonal pollution patterns (e.g., winter high pollution).
    """)

    monthly_avg = filtered_df.groupby('Month')['AQI'].mean()

    fig3, ax3 = plt.subplots()
    monthly_avg.plot(ax=ax3)
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Average AQI")
    ax3.set_title("Monthly AQI Trend")
    st.pyplot(fig3)

    # ===========================
    # GRAPH 4: POLLUTANT COMPARISON
    # ===========================
    st.subheader("🧪 Pollutant Comparison")

    st.markdown("""
    👉 Compares average levels of major pollutants.  
    👉 Helps identify which pollutant contributes most to air pollution.
    """)

    pollutants = ['PM2.5', 'PM10', 'NO2', 'CO']

    fig4, ax4 = plt.subplots()
    filtered_df[pollutants].mean().plot(kind='bar', ax=ax4)
    ax4.set_title("Average Pollutant Levels")
    st.pyplot(fig4)

# ===========================
# MODEL COMPARISON
# ===========================

st.subheader("🤖 Model Performance Comparison")

st.markdown("""
👉 This graph compares performance of different models using RMSE.  
👉 Lower RMSE means better prediction accuracy.
""")

# 🔥 Replace these values with your actual results later
model_results = {
    "XGBoost": 35,
    "Random Forest": 42,
    "LSTM": 30
}

models = list(model_results.keys())
errors = list(model_results.values())

fig5, ax5 = plt.subplots()
ax5.bar(models, errors)
ax5.set_title("Model Comparison (RMSE)")
ax5.set_ylabel("RMSE (Lower is Better)")
st.pyplot(fig5)


