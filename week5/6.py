import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales_data (2).csv')
sales['Date'] = pd.to_datetime(sales['Date'])
sales['Total_Sales'] = sales['Quantity'] * sales['Price']

# Top customers
top_customers = sales.groupby('Customer_ID')['Total_Sales'].sum().head(10)

plt.figure()
top_customers.plot(kind='bar')
plt.title("Top Customers by Sales")
plt.show()

# Regional sales
region_sales = sales.groupby('Region')['Total_Sales'].sum()

plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Region")
plt.show()

# Monthly sales
sales['Month'] = sales['Date'].dt.to_period('M')
monthly_sales = sales.groupby('Month')['Total_Sales'].sum()

plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()

# Best products
best_products = sales.groupby('Product')['Quantity'].sum()

plt.figure()
best_products.plot(kind='bar')
plt.title("Best Selling Products")
plt.show()
