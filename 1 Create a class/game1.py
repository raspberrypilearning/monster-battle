from time import sleep
from monster import Monster

# Create monsters
player_name = input("What is your monster called?")
player = Player(player_name)
bad_guy = Monster("Doombeast")

# Describe the HP of both players
player.describe()
bad_guy.describe()
sleep(3)

# Continue while both players are alive
while player.is_alive() and bad_guy.is_alive():

    # Monster's turn
    if bad_guy.is_alive():
        bad_guy.attack(player)
        player.describe()
        sleep(3)

    # Is the player now dead?
    if player.is_alive() == False:
        print("You lost :(")
    else:
        player.attack(bad_guy)
        bad_guy.describe()
        sleep(3)
        if bad_guy.is_alive() == False:
            print("You win!")
