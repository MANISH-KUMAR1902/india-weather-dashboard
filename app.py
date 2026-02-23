import streamlit as st
from data_fetch import fetch_weather
from datetime import datetime

st.set_page_config(
    page_title="India Live Weather Dashboard",
    layout="wide",
    page_icon="🌦"
)

st.title("🇮🇳 Live India Weather Dashboard")
st.caption("Real-time weather monitoring across Indian States")

# 🔐 Get API Key safely from Streamlit secrets
API_KEY = st.secrets.get("API_KEY")

if not API_KEY:
    st.error("API Key not found. Please configure secrets.")
    st.stop()


# 🔄 Auto refresh every 60 sec
st.experimental_autorefresh(interval=60000, key="refresh")

# Fetch data
df = fetch_weather(API_KEY)

if df.empty:
    st.error("⚠ Unable to fetch weather data.")
    st.stop()

# Sort by temperature
df = df.sort_values("Temperature (°C)", ascending=False)

# ---- Metrics ----
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cities", len(df))

with col2:
    hottest = df.iloc[0]
    st.metric("🔥 Hottest City", hottest["State"])

with col3:
    st.metric("Last Updated", datetime.now().strftime("%H:%M:%S"))

st.divider()

# ---- Charts ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡 Temperature by City")
    st.bar_chart(df.set_index("State")["Temperature (°C)"])

with col2:
    st.subheader("💧 Humidity by City")
    st.bar_chart(df.set_index("State")["Humidity (%)"])

st.success(
    f"🔥 Hottest Right Now: {hottest['State']} - {hottest['Temperature (°C)']}°C"
)
