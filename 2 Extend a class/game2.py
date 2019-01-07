from monster import Monster
from player import Player

# Create monsters
player_name = input("What is your monster called?")
player = Player(player_name)
bad_guy = Monster("Doombeast")

# Describe the HP of both players
player.describe()
bad_guy.describe()

# Continue while both players are alive
while player.is_alive() and bad_guy.is_alive():

    # Would you like to attack or defend?
    action = input("Would you like to attack (a) or defend (d)?")
    if action == "d":
        player.defend()

    # Monster's turn
    if bad_guy.is_alive():
        bad_guy.attack(player)
        player.describe()

    # Is the player now dead?
    if player.is_alive() == False:
        print("You lost :(")
    else:
        if action == "a":
            player.attack(bad_guy)
        elif action != "d":
            print("I don't know how to " + action)

        # Describe the outcome
        bad_guy.describe()

        if bad_guy.is_alive() == False:
            print("You win!")
            if bad_guy.get_hp() < 0:
                print("OVERKILL!")
