import pandas as pd

df = pd.read_csv("weather_data.csv")

print(df.head())
print(df.info())
print(df.describe())

# Cleaning
df = df.drop_duplicates()
df = df.fillna(method="ffill")

avg_temp = df["Temperature_C"].mean()
max_temp = df["Temperature_C"].max()

print("Average Temperature:", avg_temp)
print("Maximum Temperature:", max_temp)

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import pandas as pd

df["Date_Time"] = pd.to_datetime(df["Date_Time"])

df = df.drop_duplicates()
df = df.iloc[::10]  # reduce points

plt.figure()
plt.plot(df["Date_Time"], df["Temperature_C"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Trend")
plt.show()

