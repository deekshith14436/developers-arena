import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Shape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nBasic info:")
print(df.info())
