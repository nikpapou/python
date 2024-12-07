import matplotlib.pyplot as plt
import numpy as np

Players = ['Harry Kane', 'Mo Salah', 'Bruno Fernandes', 'Jamie Vardy', 'Son Heung-min']
Teams = ['Tottenham Hotspur', 'Liverpool', 'Manchester United', 'Leicester City', 'Tottenham Hotspur']
Goals = [23, 25, 21, 22, 19]
Assists = [8, 7, 11, 6, 10]
Games_played = [34, 33, 34, 35, 33]
Team_points = [65, 74, 70, 64, 65]

plt.figure(figsize=(12, 6))
plt.pie(Assists, labels=Players, autopct='%1.1f%%')

plt.title('Assist Distribution Among EPL Players (Session)')
plt.show()