import requests
import pandas as pd
from datetime import datetime

def fetch_weather(api_key):

    states = [
        "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore",
        "Hyderabad", "Ahmedabad", "Jaipur", "Lucknow", "Bhopal"
    ]

    weather_data = []

    for state in states:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={state},IN&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data.append({
                "State": state,
                "Temperature (°C)": data["main"]["temp"],
                "Humidity (%)": data["main"]["humidity"],
                "Condition": data["weather"][0]["main"],
                "Time": datetime.now()
            })

    return pd.DataFrame(weather_data)
