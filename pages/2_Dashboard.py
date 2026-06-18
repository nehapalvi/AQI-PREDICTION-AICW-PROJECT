# pages/2_Dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

from utils.mapping import reverse_city_mapping

st.header("📊 AQI Dashboard")

# ---------------------------
# LOAD DATA
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "eda_dataset.csv")

df = pd.read_csv(file_path)

df['datetime'] = pd.to_datetime(
    df['Year'].astype(str) + '-' +
    df['Month'].astype(str).str.zfill(2) + '-' +
    df['Day'].astype(str).str.zfill(2) + ' ' +
    df['Hour'].astype(str).str.zfill(2) + ':00:00'
)

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

    col1, col2 = st.columns(2)

    # ===========================
    # GRAPH 1: AQI TREND
    # ===========================
    with col1:
        st.subheader("📈 AQI Trend Over Time")
        fig1 = px.line(
            filtered_df, x='datetime', y='AQI',
            title="AQI Trend",
            labels={'datetime': 'Year', 'AQI': 'AQI'}
        )
        fig1.update_traces(line=dict(width=1.2))
        fig1.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("Pollution spikes and overall trend (increasing/decreasing).")

    # ===========================
    # GRAPH 2: PM2.5 vs AQI
    # ===========================
    with col2:
        st.subheader("🌫 PM2.5 vs AQI")
        fig2 = px.scatter(
            filtered_df, x='PM2.5', y='AQI',
            title="PM2.5 vs AQI",
            labels={'PM2.5': 'PM2.5', 'AQI': 'AQI'},
            opacity=0.4
        )
        fig2.update_traces(marker=dict(size=3))
        fig2.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Higher PM2.5 = higher AQI (worse air quality).")

    col3, col4 = st.columns(2)

    # ===========================
    # GRAPH 3: MONTHLY TREND
    # ===========================
    with col3:
        st.subheader("📅 Monthly Avg AQI")
        monthly_avg = filtered_df.groupby('Month')['AQI'].mean().reset_index()
        fig3 = px.line(
            monthly_avg, x='Month', y='AQI',
            title="Monthly AQI Trend",
            labels={'Month': 'Month', 'AQI': 'Avg AQI'}
        )
        fig3.update_traces(line=dict(width=1.2))
        fig3.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Seasonal pollution patterns (e.g., winter spikes).")

    # ===========================
    # GRAPH 4: POLLUTANT COMPARISON
    # ===========================
    with col4:
        st.subheader("🧪 Pollutant Comparison")
        pollutants = ['PM2.5', 'PM10', 'NO2', 'CO']
        pollutant_df = filtered_df[pollutants].mean().reset_index()
        pollutant_df.columns = ['Pollutant', 'Avg Level']
        fig4 = px.bar(
            pollutant_df, x='Pollutant', y='Avg Level',
            title="Avg Pollutant Levels"
        )
        fig4.update_layout(height=300, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig4, use_container_width=True)
        st.caption("Which pollutant contributes most to air pollution.")