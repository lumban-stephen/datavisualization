import matplotlib.pyplot as plt

players = {
    "player1": {
        "data": [10161, 13901, 10027, 12742, 8438, 7932, 12983, 9633, 8457, 11420],
        "color": 'r',
        "mColor": 'g',
        "label": "Masayoshi"
    },
    "player2": {
        "data": [6890, 9603, 9184, 10524, 11450, 9884, 9184, 11122, 8314, 11694],
        "color": 'g',
        "mColor": 'b',
        "label": "1G"
    },
    "player3": {
        "data": [11179, 10282, 13433, 8393, 11722, 10358, 10780, 9777, 17367, 8389],
        "color": 'b',
        "mColor": 'c',
        "label": "s a z"
    },
    "player4": {
        "data": [9335, 14565, 11474, 12951, 11413, 10686, 10907, 11895, 16127, 19558],
        "color": 'c',
        "mColor": 'm',
        "label": "AlbertosS"
    },
    "player5": {
        "data": [8983, 8527, 8473, 11746, 10049, 11808, 9310, 14229, 11194, 9904],
        "color": 'm',
        "mColor": 'r',
        "label": "Paul"
    }
}

# Create a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Flatten the axes array to make it easier to work with
axes = axes.flatten()

# Extract data and labels for all players
playerData = [player["data"] for player in players.values()]
playerLabels = [player["label"] for player in players.values()]
playerColors = [player["color"] for player in players.values()]
markerColor = [player["mColor"] for player in players.values()]

gameNumber = list(range(1, 11))

# Plot data for all players in subplots
for i, (data, color, mColor, label) in enumerate(zip(playerData, playerColors, markerColor, playerLabels)):
    ax = axes[i]
    ax.plot(gameNumber, data, marker='D', linestyle='--', color=color, markerfacecolor=mColor, label=label)
    ax.set_xlabel('Game Number')
    ax.set_ylabel("Net worth In Game")
    ax.set_title(f'{label}\'s Performance')
    ax.legend()

# Remove any unused subplots
for i in range(len(playerData), len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
fig = plt.figure(1)
fig.patch.set_facecolor("c")
plt.show()