import pandas as pd

df = pd.read_csv("sales_data.csv")


print("Missing values before cleaning:")
print(df.isnull().sum())


df.fillna(0, inplace=True)


df.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nData cleaned successfully!")
