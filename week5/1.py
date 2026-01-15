import pandas as pd

# Load datasets
sales = pd.read_csv('sales_data (2).csv')
churn = pd.read_csv('customer_churn.csv')

# Basic exploration
print("Sales Data Info")
print(sales.info())
print("\nSales Data Preview")
print(sales.head())

print("\nChurn Data Info")
print(churn.info())
print("\nChurn Data Preview")
print(churn.head())

# Check missing values
print("\nMissing Values in Sales Data")
print(sales.isnull().sum())

print("\nMissing Values in Churn Data")
print(churn.isnull().sum())
