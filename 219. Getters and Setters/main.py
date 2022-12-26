import player

tim = player.Player("Tim")
# tim = Player("Tim")
print("*"*60)
print("Player name : {}".format(tim.name))
print("Lives : {}".format(tim.lives))
tim.lives -= 1
print("Lives : {}".format(tim))
print("*"*60)
tim.lives -= 1
print("Lives : {}".format(tim))
print("*"*60)
tim.lives -= 1
print("Lives : {}".format(tim))
print("*"*60)
tim.lives -= 1
print("Lives : {}".format(tim))
print("*"*60)
