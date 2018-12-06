from monster import Monster

# Create monsters
player = Monster("Laura the fearsome")
opponent = Monster("Grumpatron")

# Start game loop
game_in_progress = True
while game_in_progress:

    # Describe the HP of both players
    player.describe()
    opponent.describe()
    input("...")
    print("--------- oOo ---------")

    # Player's attack
    player.attack(opponent)

    # Monster's attack
    if opponent.is_alive() == True:
        opponent.attack(player)
        if player.is_alive() == False:
            print("YOU LOSE")
            game_in_progress = False
    else:
        print("YOU WIN")
        game_in_progress = False





    input("...")
