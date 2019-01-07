from monster import Monster
from player import Player

# Create monsters
player = Player("Laura the fearsome")
opponent = Monster("Grumpatron")

# Continue while both players are alive
while player.is_alive() and opponent.is_alive():

    # Describe the HP of both players
    player.describe()
    opponent.describe()
    input("> Press Enter <")

    # Player's turn
    if player.is_alive():

        player.reset_defence()
        
        # Would you like to attack or defend?
        action = input("Would you like to attack (a) or defend (d)?")
        if action == "a":
            player.attack(opponent)
        elif action == "d":
            player.defend()
        else:
            print("You failed to " + action)

        # Monster's attack
        if opponent.is_alive():
            opponent.attack(player)

            # Is the player now dead?
            if player.is_alive() == False:
                print("You lost :(")
        else:
            print("You win!")

    input("> Press Enter <")
