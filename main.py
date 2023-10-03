import matplotlib.pyplot as plt
import numpy as np

# Define player data as a dictionary with associated colors
players = {
    "player1": ([500, 400, 900, 600, 800, 700, 200, 550, 500, 620], 'r', 'g'),  # 'r' for red
    "player2": ([500, 400, 900, 600, 800, 700, 200, 550, 500, 620], 'g', 'b'),  # 'g' for green
    "player3": ([500, 400, 900, 600, 800, 700, 200, 550, 500, 620], 'b', 'c'),  # 'b' for blue
    "player4": ([500, 400, 900, 600, 800, 700, 200, 550, 500, 620], 'c', 'm'),  # 'c' for cyan
    "player5": ([500, 400, 900, 600, 800, 700, 200, 550, 500, 620], 'm', 'r')   # 'm' for magenta
}

username = input("Enter username: ")

if username in players:
    player_data, color, mColor = players[username]

    gameNumber = list(range(1, 11))
    plt.plot(gameNumber, player_data, marker='D', linestyle='--', color=color, markerfacecolor=mColor)
    plt.xlabel(f'Last 10 Games of {username}')
    plt.ylabel(f"{username}'s Net worth In Game")
    plt.title(f'{username} Performance Over 10 Games')
    plt.show()
else:
    print(f"No data found for username: {username}")
