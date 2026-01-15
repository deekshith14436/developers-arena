import pandas as pd

sales = pd.read_csv('sales_data (2).csv')
sales['Total_Sales'] = sales['Quantity'] * sales['Price']

# Top customers by lifetime value
top_customers = (
    sales.groupby('Customer_ID')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 Customers by Sales")
print(top_customers)

# Regional customer distribution
region_sales = sales.groupby('Region')['Total_Sales'].sum()
print("\nSales by Region")
print(region_sales)
