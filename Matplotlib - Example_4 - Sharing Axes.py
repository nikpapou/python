import matplotlib.pyplot as plt
import numpy as np

players = ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.', 'Kylian Mbappe', 'Robert Lewandowski']
goals = [36, 34, 21, 33, 41]
assists = [12, 7, 10, 7, 5]
dribbles = [174, 89, 142, 90, 41]

# Create a 1x2 subplot grid with shared Y-axis
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(12, 6))


# First subplot: bar plot for values1
ax[0].bar(players, goals, color='blue')
ax[0].set_ylabel("Goals")
ax[0].grid(True)
plt.arrow(4, 41, 0, 0, length_includes_head=False, head_width=0.5, head_length=2, color='red')

# Second subplot: bar plot for values2
ax[1].bar(players, assists, color='red')
ax[1].set_ylabel("Assists")
ax[1].grid(True)

ax[2].bar(players, dribbles, color='purple')
ax[2].set_ylabel("Succesful Dribbles")
ax[2].grid(True)

plt.subplots_adjust(hspace=0.6)

plt.tight_layout()
plt.show()