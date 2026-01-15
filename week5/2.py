import pandas as pd

sales = pd.read_csv('sales_data (2).csv')

# Convert Date column
sales['Date'] = pd.to_datetime(sales['Date'], errors='coerce')

# Remove missing values
sales.dropna(inplace=True)

# Create calculated column
sales['Total_Sales'] = sales['Quantity'] * sales['Price']

print("Cleaned Sales Data")
print(sales.head())
