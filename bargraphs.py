import matplotlib.pyplot as plt

def getMean(data_list):
    return sum(data_list) / len(data_list)

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

fig = plt.figure(figsize=(10, 5))

playerLabels = [player["label"] for player in players.values()]
playerData = [player["data"] for player in players.values()]
playerColors = [player["color"] for player in players.values()]

# Calculate the mean for each player's data
playerMeans = [getMean(data) for data in playerData]

# Creating the bar plot
plt.bar(playerLabels, playerMeans, color=playerColors)

plt.xlabel("Players")
plt.ylabel("Net Worth in Gold")
plt.title("ML Players' Average in 10 Games")
plt.show()