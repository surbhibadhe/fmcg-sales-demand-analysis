import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel file
df = pd.read_excel("fmgc.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("%", "percent")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Create month and day columns
df['month'] = df['date'].dt.month_name()
df['day_name'] = df['date'].dt.day_name()

# Create Nestlé-style category column
category_map = {
    'Health and beauty': 'Nutrition & Wellness',
    'Electronic accessories': 'Coffee & Ready-to-Drink',
    'Home and lifestyle': 'Dairy & Daily Essentials',
    'Sports and travel': 'Confectionery & Snacks',
    'Food and beverages': 'Packaged Foods & Beverages',
    'Fashion accessories': 'Cereals & Kids Nutrition'
}

df['nestle_category'] = df['product_line'].map(category_map)

# Create sales channel column
channel_map = {
    'Member': 'Modern Trade',
    'Normal': 'General Trade'
}

df['sales_channel'] = df['customer_type'].map(channel_map)

# Create demand level column
conditions = [
    df['quantity'] >= 8,
    (df['quantity'] >= 4) & (df['quantity'] < 8),
    df['quantity'] < 4
]

choices = ['High Demand', 'Medium Demand', 'Low Demand']

df['demand_level'] = np.select(conditions, choices, default='Low Demand')

# ---------------- KPI ANALYSIS ----------------

print("\nTOTAL SALES:")
print(round(df['sales'].sum(), 2))

print("\nTOTAL GROSS INCOME:")
print(round(df['gross_income'].sum(), 2))

print("\nTOTAL QUANTITY SOLD:")
print(df['quantity'].sum())

print("\nTOP CATEGORY BY SALES:")
category_sales = df.groupby('nestle_category')['sales'].sum().sort_values(ascending=False)
print(category_sales)

print("\nSALES BY CHANNEL:")
channel_sales = df.groupby('sales_channel')['sales'].sum().sort_values(ascending=False)
print(channel_sales)

print("\nSALES BY CITY:")
city_sales = df.groupby('city')['sales'].sum().sort_values(ascending=False)
print(city_sales)

print("\nSALES BY BRANCH:")
branch_sales = df.groupby('branch')['sales'].sum().sort_values(ascending=False)
print(branch_sales)

print("\nDEMAND LEVEL COUNT:")
print(df['demand_level'].value_counts())

print("\nCATEGORY-WISE QUANTITY SOLD:")
category_quantity = df.groupby('nestle_category')['quantity'].sum().sort_values(ascending=False)
print(category_quantity)

print("\nAVERAGE RATING BY CATEGORY:")
category_rating = df.groupby('nestle_category')['rating'].mean().sort_values(ascending=False)
print(category_rating)

# ---------------- VISUALIZATIONS ----------------

sns.set(style="whitegrid")

# 1. Category sales chart
plt.figure(figsize=(10,6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Nestlé Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 2. Sales by channel
plt.figure(figsize=(6,4))
channel_sales.plot(kind='bar', color=['orange', 'green'])
plt.title('Sales by Channel')
plt.xlabel('Sales Channel')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("channel_sales.png")
plt.show()

# 3. Sales by city
plt.figure(figsize=(8,5))
city_sales.plot(kind='bar', color='purple')
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("city_sales.png")
plt.show()

# Save transformed dataset
df.to_excel("nestle_fmcg_transformed.xlsx", index=False)

print("\nDone - analysis and charts created successfully")


# Correct month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

monthly_sales = df.groupby('month')['sales'].sum()

# 4. Monthly sales trend
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', color='red')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# 5. Category-wise quantity sold
plt.figure(figsize=(10,6))
category_quantity.plot(kind='bar', color='teal')
plt.title('Category-wise Quantity Sold')
plt.xlabel('Category')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_quantity.png")
plt.show()

# 6. Average rating by category
plt.figure(figsize=(10,6))
category_rating.plot(kind='bar', color='coral')
plt.title('Average Rating by Category')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_rating.png")
plt.show()

# 7. Demand level distribution
plt.figure(figsize=(6,4))
df['demand_level'].value_counts().plot(kind='bar', color=['darkgreen', 'orange', 'red'])
plt.title('Demand Level Distribution')
plt.xlabel('Demand Level')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("demand_level_distribution.png")
plt.show()