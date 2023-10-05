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

playerData = [player["data"] for player in players.values()]
playerLabel = [player["label"] for player in players.values()]
playerColors = [player["color"] for player in players.values()]
markerColors = [player["mColor"] for player in players.values()]

gameNumber = list(range(1, 11))

for data, color, mColor, label in zip(playerData, playerColors, markerColors, playerLabel):
    plt.plot(gameNumber, data, marker='D', linestyle='--', color=color, markerfacecolor=mColor, label=label)



plt.xlabel("Game Number")
plt.ylabel("Net Worth in-game")
plt.title("Net worth of Players over 10 Games")
plt.legend()
fig = plt.figure(1)
fig.patch.set_facecolor("c")
plt.show()
