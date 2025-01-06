import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/nikpa/OneDrive/Documents/NIKOS/ΣΠΟΥΔΕΣ/ΣΕΜΙΝΑΡΙΑ/Data Analysis/Workearly/Healthcare Analytics Bootcamp/Python/Assignments & Case Studies/Datasets/movies.csv")
#print(df)
#print(df.head())
print(df.isnull().sum())

# Remoce Rows with Missing Values
df.dropna(inplace=True)
# Convert the budget and revenue columns to numeric types
df['budget'] = pd.to_numeric(df['budget'])
df['revenue'] = pd.to_numeric(df['revenue'])
# Create a new column profit
df['profit'] = df['revenue'] - df['budget']
# Calculate summary statistics
budget_stats = df['budget'].describe()
revenue_stats = df['revenue'].describe()
profit_stats = df['profit'].describe()
print('\nBudget Stats:\n', budget_stats)
print('\nRevenue Stats:\n', revenue_stats)
print('\nProfit Stats:\n', profit_stats)

# Histogram for the profit column
plt.hist(df['profit'], bins=20)
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.title('Distribution of Profit')
plt.show()
# Scatter plot for budget versus revenue
plt.scatter(df['budget'], df['revenue'])
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.title('Budget vs Revenue')
plt.show()