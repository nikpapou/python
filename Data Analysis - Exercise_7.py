import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/nikpa/OneDrive/Documents/NIKOS/ΣΠΟΥΔΕΣ/ΣΕΜΙΝΑΡΙΑ/Data Analysis/Workearly/Healthcare Analytics Bootcamp/Python/Assignments & Case Studies/Datasets/vgsales.csv")
# print(df)
# print(df.head())
# print(df.info())
# print(df.shape)


# drop rows with missing values
# print(df.isnull().sum())
df.dropna(inplace=True)

# group data by game name and sum global sales
game_sales = df.groupby('Name')['Global_Sales'].sum()
# sort by global sales
game_sales = game_sales.sort_values(ascending=False)
# display top 10 games
print(game_sales.head(10))

# most popular platform
platform_sales = df.groupby('Platform')['Global_Sales'].sum()
platform_sales = platform_sales.sort_values(ascending=False)
print('\nplatform_sales', platform_sales)

# Which genre is the most popular?
most_famous_genre = df.groupby('Genre')['Global_Sales'].sum()
most_famous_genre = most_famous_genre.sort_values(ascending=False)
print(most_famous_genre)

# How do sales vary by region?
region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
region_sales.plot(kind='bar')
plt.title('Video Game Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales (millions)')
plt.show()

# Is there a relationship between the year of release and sales?
plt.scatter(df['Year'], df['Global_Sales'])
plt.title('Year of Release vs Global Sales')
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.show()

# Is there a relationship between publisher and sales?
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()
publisher_sales = publisher_sales.sort_values(ascending=False)
publisher_sales.head(10).plot(kind='bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()
