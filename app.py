import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="India Weather Dashboard", layout="wide")
st.title("🇮🇳 Live India Weather Dashboard")

file_path = "weather_data.csv"
refresh_interval = 10

# Read CSV
df = pd.read_csv(file_path)

# Clean columns
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace("Â", "")

# Convert time automatically
df["Time"] = pd.to_datetime(df["Time"])

# Get latest record per state
latest_df = df.sort_values("Time").groupby("State").tail(1)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡 Temperature by State")
    st.bar_chart(latest_df.set_index("State")["Temperature (°C)"])

with col2:
    st.subheader("💧 Humidity by State")
    st.bar_chart(latest_df.set_index("State")["Humidity (%)"])

max_row = latest_df.loc[latest_df["Temperature (°C)"].idxmax()]
st.success(
    f"🔥 Hottest State Right Now: {max_row['State']} - {max_row['Temperature (°C)']}°C"
)

time.sleep(refresh_interval)
st.rerun()
