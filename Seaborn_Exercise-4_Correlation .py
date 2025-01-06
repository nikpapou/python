import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define a dictionary containing data
data = {
    "Height": [170, 168, 177, 181, 176],
    "Weight": [72, 67, 78, 79, 73],
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))

# Create a scatter plot with a regression line using seaborn
sns.regplot(x="Height", y="Weight", data=df, marker="o", scatter_kws={"s": 200, "alpha": 0.5})
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.show()  