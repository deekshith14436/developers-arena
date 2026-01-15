import pandas as pd

sales = pd.read_csv('sales_data (2).csv')
churn = pd.read_csv('customer_churn.csv')

sales['Total_Sales'] = sales['Quantity'] * sales['Price']

# Pivot table: Region vs Product
pivot_table = pd.pivot_table(
    sales,
    values='Total_Sales',
    index='Region',
    columns='Product',
    aggfunc='sum'
)

print("Pivot Table: Region vs Product")
print(pivot_table)

# Merge churn data
merged_data = sales.merge(
    churn,
    left_on='Customer_ID',
    right_on='CustomerID',
    how='left'
)

# Retention rate
retention_rate = 1 - merged_data['Churn'].mean()
print("\nCustomer Retention Rate:", retention_rate)
