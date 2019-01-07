from monster import Monster

# Create monsters
player_name = input("What is your monster called?")
you = Monster(player_name)
bad_guy = Monster("Doombeast")

# Describe the HP of both players
you.describe()
bad_guy.describe()

# Continue while both players are alive
while you.is_alive() and bad_guy.is_alive():

    # Monster's turn
    if bad_guy.is_alive():
        bad_guy.attack(you)
        you.describe()

    # Is the player now dead?
    if you.is_alive() == False:
        print("You lost :(")
    else:
        you.attack(bad_guy)

        # Describe the outcome
        bad_guy.describe()

        if bad_guy.is_alive() == False:
            print("You win!")
            if bad_guy.get_hp() < 0:
                print("OVERKILL!")
