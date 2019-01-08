from monster import Monster
from player import Player

# Create monsters
player_name = input("What is your monster called?")
you = Player(player_name)
bad_guy = Monster("Doombeast")

# Describe the HP of both players
you.describe()
you.describe_item()
bad_guy.describe()
bad_guy.describe_item()


# Continue while both players are alive
while you.is_alive() and bad_guy.is_alive():

    # Would you like to attack or defend?
    action = input("Would you like to attack (a) or defend (d)?")
    if action == "d":
        you.defend()

    # Monster's turn
    if bad_guy.is_alive():
        bad_guy.attack(you)
        you.describe()

    # Is the player now dead?
    if you.is_alive() == False:
        print("You lost :(")
    else:
        if action == "a":
            you.attack(bad_guy)
        elif action != "d":
            print("I don't know how to " + action)

        # Describe the outcome
        bad_guy.describe()

        if bad_guy.is_alive() == False:
            print("You win!")
            if bad_guy.get_hp() < 0:
                print("OVERKILL!")
