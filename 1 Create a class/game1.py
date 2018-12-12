from monster import Monster

# Create monsters
player = Monster("Laura the fearsome")
opponent = Monster("Grumpatron")

# Continue while both players are alive
while player.is_alive() and opponent.is_alive():

    # Describe the HP of both players
    player.describe()
    opponent.describe()
    input("> Press Enter <")

    # Player's attack
    if player.is_alive():
        player.attack(opponent)

        # Monster's attack
        if opponent.is_alive():
            opponent.attack(player)

            # Is the player now dead?
            if player.is_alive() == False:
                print("You lost :(")
        else:
            print("You win!")

    input("> Press Enter <")
