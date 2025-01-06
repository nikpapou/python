import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
 '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
  'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
  'Revenue': [100, 200, 150, 300, 120, 250, 170, 350, 110, 280]}
df = pd.DataFrame(data)

#print(df)
total_revenue = np.sum(df['Revenue'])
print("Total Revenue: ", total_revenue)
average_revenue = np.average(df['Revenue'])
print("Average Revenue: ", average_revenue)

# Calculate the total revenue for each product
product_revenue = df.groupby('Product')['Revenue'].sum()
print("\nRevenue per Product: \n", product_revenue)

# Bar chart of total revenue per product
fig, ax = plt.subplots()
ax.bar(product_revenue.index, product_revenue.values)
ax.set_xlabel('Product')
ax.set_ylabel('Revenue')
ax.set_title('Total Revenue per Product')
plt.show()
# Line chart of daily revenue
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Revenue'])
ax.set_xlabel('Date')
ax.set_ylabel('Revenue')
ax.set_title('Daily Revenue')
plt.xticks(rotation=45)
plt.show()




