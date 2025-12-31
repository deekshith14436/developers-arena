import pandas as pd

df = pd.read_csv("sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]

total_revenue = df["Revenue"].sum()
best_product = df.groupby("Product")["Revenue"].sum().idxmax()
best_product_revenue = df.groupby("Product")["Revenue"].sum().max()

print("===== SALES REPORT =====")
print(f"Total Revenue Generated: {total_revenue}")
print(f"Top Performing Product: {best_product}")
print(f"Revenue from Best Product: {best_product_revenue}")


