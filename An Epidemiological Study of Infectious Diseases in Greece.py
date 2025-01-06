import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/nikpa/OneDrive/Documents/NIKOS/ΣΠΟΥΔΕΣ/ΣΕΜΙΝΑΡΙΑ/Data Analysis/Workearly/Healthcare Analytics Bootcamp/Python/Assignments & Case Studies/Datasets/2-greece_infectious_diseases_indicators.csv")
# print(df)
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.shape)

# drop rows with missing values
print(df.isnull().sum())

# Task 1
sns.set_style("whitegrid")
plt.figure(figsize=(14, 8))
sns.lineplot(x='YEAR', y='CASES', hue='NAME', data=df, marker='o')
plt.title('Reported Cases of Infectious Diseases in Greece Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.legend(title='Disease', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Task 2
# Total cases per disease
total_cases_per_disease = df.groupby('NAME')['CASES'].sum()
# Select the top 5 diseases
top_diseases = total_cases_per_disease.sort_values(ascending=False).head(5)

# Graph
plt.figure(figsize=(10, 6))
sns.barplot(x=top_diseases.values, y=top_diseases.index, palette="viridis")
plt.title('Top 5 Diseases with Highest Number of Cases in Greece')
plt.xlabel('Total Number of Cases')
plt.ylabel('Disease')
plt.show()

# Task 3
# Define a function to categorize years into periods
def categorize_into_periods(year, period_length=10):
    return f"{(year // period_length) * period_length}s"

# Create a new 'Period' column
df['Period'] = df['YEAR'].apply(categorize_into_periods)
df_period_sum = df.groupby(['NAME', 'Period'])['CASES'].sum().reset_index()

# Pivot the table to have periods as columns
df_pivot = df_period_sum.pivot(index='NAME', columns='Period', values='CASES').fillna(0)
# Calculate the correlation matrix
correlation_matrix = df_pivot.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Infectious Diseases by Periods')
plt.ylabel('Period')
plt.xlabel('Period')
plt.show()