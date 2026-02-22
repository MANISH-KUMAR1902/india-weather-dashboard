import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Vikas\Desktop\weather dashboard\weather_data.csv"

df = pd.read_csv(file_path)

# Latest time ka data
latest_time = df["Time"].max()
latest_df = df[df["Time"] == latest_time]

plt.figure()
plt.bar(latest_df["State"], latest_df["Temperature (°C)"])
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Temperature (°C)")
plt.title("India Temperature - Latest Data")
plt.tight_layout()
plt.show()
