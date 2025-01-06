import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv("C:/Users/nikpa/OneDrive/Documents/NIKOS/ΣΠΟΥΔΕΣ/ΣΕΜΙΝΑΡΙΑ/Data Analysis/Workearly/Healthcare Analytics Bootcamp/Python/Assignments & Case Studies/Datasets/sales_data2.csv")
#print(df)
#print(df.head())
#print(sales_data.isnull().sum())

# Calculate total revenue
total_revenue = (sales_data["price"] * sales_data["quantity"]).sum()
print(f"Total Revenue: ${total_revenue}")
# Calculate the average order value
avg_order_value = sales_data.groupby("order_id")["price"].sum().mean()
print(f"Average Order Value: ${avg_order_value:.2f}")

#Identify the top-selling products.
# Calculate product sales
product_sales = sales_data.groupby("product_id").agg({"quantity": "sum"}).reset_index()
# Sort the products by sales in descending order
product_sales = product_sales.sort_values(by="quantity", ascending=False)
# Get the top 5 selling products
top_selling_products = product_sales.head(5)
print("Top 5 Selling Products:")
print(top_selling_products)

# Bar chart
plt.bar(top_selling_products["product_id"], top_selling_products["quantity"])
plt.xlabel("Product ID")
plt.ylabel("Quantity Sold")
plt.title("Top 5 Selling Products")
plt.show()
