import pandas as pd

df = pd.read_csv("sales_data.csv")


df["Revenue"] = df["Quantity"] * df["Price"]

# Total revenue
total_revenue = df["Revenue"].sum()


best_product = df.groupby("Product")["Revenue"].sum().idxmax()

print(f"Total Revenue: {total_revenue}")
print(f"Best Selling Product: {best_product}")
