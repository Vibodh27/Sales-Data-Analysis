# Sales Data Analysis using Python and Pandas

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv('sales_data.csv')  # Make sure 'sales_data.csv' is in the same folder

# Step 2: Clean the data
df = df.dropna()  # Remove rows with missing values
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')  # Convert to datetime format
df = df.dropna(subset=['Order Date'])  # Remove rows where Order Date couldn't be parsed
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
df['Price of Each product'] = pd.to_numeric(df['Price of Each product'], errors='coerce')
df = df.dropna(subset=['Quantity Ordered', 'Price of Each product'])  # Remove rows with invalid numbers

# Step 3: Add new helpful columns
df['Month'] = df['Order Date'].dt.month
df['Sales'] = df['Quantity Ordered'] * df['Price of Each product']
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip() if isinstance(x, str) else None)

# Step 4: Analysis

# 4.1 Total sales per month
monthly_sales = df.groupby('Month').sum(numeric_only=True)
print("Monthly Sales:\n", monthly_sales['Sales'])

# Plotting monthly sales
months =  monthly_sales.index
plt.figure(figsize=(8, 5))
plt.bar(months, monthly_sales['Sales'])
plt.xticks(months)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales in IND')
plt.tight_layout()
plt.show()

# 4.2 Sales by city
city_sales = df.groupby('City').sum(numeric_only=True)
print("\nSales by City:\n", city_sales['Sales'])

# Plotting city sales
plt.figure(figsize=(10, 5))
plt.bar(city_sales.index, city_sales['Sales'])
plt.xticks(rotation=45)
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales in IND')

plt.tight_layout()
plt.show()

# 4.3 Most sold product
product_group = df.groupby('Product').sum(numeric_only=True)
print("\nMost Sold Products:\n", product_group['Quantity Ordered'].sort_values(ascending=False))

# Plotting most sold products
plt.figure(figsize=(10, 5))
plt.bar(product_group.index, product_group['Quantity Ordered'])
plt.xticks(rotation=90)
plt.title('Most Sold Products')
plt.xlabel('Product')
plt.ylabel('Quantity Ordered')
plt.tight_layout()
plt.show()
