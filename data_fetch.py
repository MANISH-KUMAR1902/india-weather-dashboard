import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests
import pandas as pd
import os
import time
from datetime import datetime

# 🔑 Apni OpenWeather API key yaha daalo
API_KEY = "c38df1699e3380ada48c11c2673244ce"

# 📁 CSV file path
file_path = r"C:\Users\Vikas\Desktop\weather dashboard\weather_data.csv"

# 🇮🇳 All 28 States + 8 Union Territories
states = {
    # 🔹 States (28)
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",

    # 🔹 Union Territories (8)
    "Andaman and Nicobar Islands": "Port Blair",
    "Chandigarh (UT)": "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu": "Daman",
    "Delhi (UT)": "New Delhi",
    "Jammu and Kashmir": "Srinagar",
    "Ladakh": "Leh",
    "Lakshadweep": "Kavaratti",
    "Puducherry": "Puducherry"
}

all_data = []

print("Fetching weather data for India...\n")

for state, city in states.items():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # API error handling
        if response.status_code != 200:
            print(f"❌ Failed for {state}: {data.get('message', 'Unknown error')}")
            continue

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        all_data.append([state, city, time_now, temp, humidity])

        print(f"✅ {state} data fetched")

        # ⚠ Humidity Alert
        if humidity > 80:
            print(f"⚠ ALERT: {state} humidity above 80%")

        time.sleep(1)  # API rate limit safety

    except Exception as e:
        print(f"❌ Error fetching {state}: {e}")

# 📊 Create DataFrame
df_new = pd.DataFrame(
    all_data,
    columns=["State", "City", "Time", "Temperature (°C)", "Humidity (%)"]
)

# 🛑 Remove duplicates if file exists
if os.path.exists(file_path):
    df_old = pd.read_csv(file_path)
    df_final = pd.concat([df_old, df_new]).drop_duplicates(subset=["State", "Time"])
else:
    df_final = df_new

# 💾 Save clean CSV (overwrite mode)
df_final.to_csv(file_path, index=False)

print("\n🎉 All India Weather Data Saved Successfully!")
