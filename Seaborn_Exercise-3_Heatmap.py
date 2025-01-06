import pandas as pd  # Importing the pandas library for data manipulation
import seaborn as sns  # Importing the seaborn library for data visualization
import matplotlib.pyplot as plt  # Importing the pyplot module from matplotlib for creating plots

sns.set_theme()

data = {
    "Goals": [15, 8, 12, 20, 5],
    "Assists": [10, 12, 8, 5, 15],
    "Appearances": [38, 35, 30, 32, 40],
    "Minutes_Played": [3420, 3150, 2700, 2880, 3600],
}
players = ["Player1", "Player2", "Player3", "Player4", "Player5"]
df = pd.DataFrame(data, index=players)

normalized_df = (df - df.min()) / (df.max() - df.min())
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(normalized_df, annot=True, cmap="coolwarm", ax=ax)
plt.show()  # Displaying the plot