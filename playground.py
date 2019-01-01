from player import Player

player_1 = Player()
print(player_1)

for round in range(10):
    player_1.round_end_update()
    print(player_1.inventory)

