
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Data Cleaning
# Convert date columns to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Handling missing values (if any)
df = df.dropna()

# Feature Engineering
df['Total Sales'] = df['Quantity'] * df['Sales']
df['Profit Margin'] = df['Profit'] / df['Total Sales']

# Exploratory Data Analysis (EDA)
# Sales trend over time
sales_trend = df.groupby('Order Date')['Total Sales'].sum().reset_index()

# Plot sales trend
fig = px.line(sales_trend, x='Order Date', y='Total Sales', title='Sales Trend Over Time')
fig.show()

# Sales by Product Category
category_sales = df.groupby('Category')['Total Sales'].sum().reset_index()

# Plot sales by category
fig = px.bar(category_sales, x='Category', y='Total Sales', title='Sales by Product Category')
fig.show()

# Relationship between Discount and Sales
fig = px.scatter(df, x='Discount', y='Total Sales', title='Discount vs Total Sales')
fig.show()

# Profit Margin by Region
region_profit = df.groupby('Region')['Profit Margin'].mean().reset_index()

# Plot profit margin by region
fig = px.bar(region_profit, x='Region', y='Profit Margin', title='Profit Margin by Region')
fig.show()

# Save the processed data to a new CSV file for Power BI
df.to_csv('Processed_Superstore_Sales.csv', index=False)
