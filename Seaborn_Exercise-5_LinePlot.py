import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Sales": [50, 58, 66, 74, 85, 96],
    "Expenses": [30, 35, 40, 45, 50, 55],
}

df = pd.DataFrame(data)

sns.set(style="darkgrid", palette="Set2")
plt.figure(figsize=(10, 6))

sns.lineplot(data=df["Sales"], marker="o", markersize=10, linewidth=2)
sns.lineplot(data=df["Expenses"], marker="o", markersize=10, linewidth=2)

plt.title("Company Performance Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Count (in 1000s)", fontsize=12)
plt.legend(labels=["Sales", "Expenses"])

plt.show()