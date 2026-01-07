import pandas as pd

df = pd.read_csv("weather_data.csv")

print(df.head())
print(df.info())
print(df.describe())

# Cleaning
df = df.drop_duplicates()
df = df.fillna(method="ffill")



