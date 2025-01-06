import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/nikpa/OneDrive/Documents/NIKOS/ΣΠΟΥΔΕΣ/ΣΕΜΙΝΑΡΙΑ/Data Analysis/Workearly/Healthcare Analytics Bootcamp/Python/Datasets/sales_data1.csv")

#print(data.info())
#print("Missing Data:\n", data.isna().sum())

# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"])
# Add a day of the week column
data["Day_of_Week"] = data["Date"].dt.day_name()
print(data)
print("\nSummary Statistics: \n", data.describe())

# Group by Product and calculate total revenue and quantity sold
product_summary = data.groupby("Product").agg({"Revenue": "sum", "Quantity": "sum"})
print("\nProduct Summary: \n", product_summary)

product_summary["Revenue"].plot(kind="bar")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue per Product")
plt.show()