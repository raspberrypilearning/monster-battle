from monster import Monster
from player import Player

# Main game
# Create your player object, each player has a companion
laura = Player()
print("Your monster is called " + laura.companion_name())
laura.companion.status()
print("------------------")

# Create a monster to fight
opponent = Monster()
print( "Your opponent is a monster called " + opponent.get_name())

end_game = False
while end_game == False:
    move = laura.get_action()
    laura.do_action(move, opponent)
    print("opponent" + str(opponent.is_alive()))
    print("you" + str(laura.companion.is_alive()))
    if opponent.is_alive() and laura.companion.is_alive():
        opponent.fight(laura)
    else:
        end_game = True

    



