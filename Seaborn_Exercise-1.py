import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "team": ["Barcelona", "Real Madrid", "Atletico Madrid", "Sevilla", "Villarreal"],
    "goals": [86, 67, 58, 54, 60],
}

soccer_data = pd.DataFrame(data)

sns.set_style("darkgrid")
sns.set_palette("husl")

sns.scatterplot(x="team", y="goals", data=soccer_data, marker="s", s=100)
plt.xticks(rotation=15)
plt.title("Goals Scored by Teams")
plt.xlabel("Team")
plt.ylabel("Goals")
plt.show()