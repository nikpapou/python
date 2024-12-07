import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

Goals_Scored = [45, 52, 48, 42, 50]
Assists = [20, 15, 18, 23, 22]
Minutes_Played = [2800, 2900, 2750, 2700, 2850]


fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Goals_Scored, Assists, Minutes_Played, color='red', marker='o')

ax.set_xlabel('Goals Scored', fontsize=14)
ax.set_ylabel('Assists', fontsize=14)
ax.set_zlabel('Minutes Played', fontsize=14)

plt.title('3D of Scatter Plot of Goals, Assits and minutes Played', fontsize = 20)
plt.show()