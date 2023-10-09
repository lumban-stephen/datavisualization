import matplotlib.pyplot as plt

#Player 1
player1 = [10161, 13901, 10027, 12742, 8438, 7932, 12983, 9633, 8457, 11420]
player1max = max(player1)
player1min = min(player1)
plt.scatter(player1min, player1min, marker='x',  color="r", label="Masayoshi")
plt.scatter(player1max, player1max, marker='x',  color="r")

#Player2
player2 = [6890, 9603, 9184, 10524, 11450, 9884, 9184, 11122, 8314, 11694]
player2max = max(player2)
player2min = min(player2)
plt.scatter(player2min, player2min, marker='D',  color="g", label="1G")
plt.scatter(player2max, player2max, marker='D',  color="g")

#Player3
player3 = [11179, 10282, 13433, 8393, 11722, 10358, 10780, 9777, 17367, 8389]
player3max = max(player3)
player3min = min(player3)
plt.scatter(player3min, player3min, marker='*',  color="b", label="s a z")
plt.scatter(player3max, player3max, marker='*',  color="b")

#Player4
player4 = [9335, 14565, 11474, 12951, 11413, 10686, 10907, 11895, 16127, 19558]
player4max = max(player4)
player4min = min(player4)
plt.scatter(player4min, player4min, marker='o',  color="c", label="AlbertosS")
plt.scatter(player4max, player4max, marker='o',  color="c")

#Player5
player5 = [8983, 8527, 8473, 11746, 10049, 11808, 9310, 14229, 11194, 9904]
player5max = max(player5)
player5min = min(player5)
plt.scatter(player5min, player5min, marker='+',  color="m", label="Paul")
plt.scatter(player5max, player5max, marker='+',  color="m")


plt.xlabel("Net Worth in-game")
plt.ylabel("Net Worth in-game")
plt.title("Net worth of Players Minimum and Maximum over 10 Games")
plt.legend()
fig = plt.figure(1)
fig.patch.set_facecolor("c")
plt.show()


