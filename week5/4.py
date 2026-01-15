import pandas as pd

sales = pd.read_csv('sales_data (2).csv')
sales['Date'] = pd.to_datetime(sales['Date'])
sales['Total_Sales'] = sales['Quantity'] * sales['Price']

# Monthly sales trend
sales['Month'] = sales['Date'].dt.to_period('M')
monthly_sales = sales.groupby('Month')['Total_Sales'].sum()

print("Monthly Sales Trend")
print(monthly_sales)

# Best selling products
best_products = (
    sales.groupby('Product')['Quantity']
    .sum()
    .sort_values(ascending=False)
)

print("\nBest Selling Products")
print(best_products)
