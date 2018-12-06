import random
from monster import Monster

class Player():
    
    # Constructor
    def __init__(self):
        self.actions = ["attack", "retreat", "defend"]
        self.companion = Monster()
    
    def get_actions(self):
        return self.actions
    
    def get_companion(self):
        return self.companion

    def companion_name(self):
        return self.companion.get_name()
    
    # Get a desired action from the user
    def get_action(self):
        print( "You can " + str(self.actions) )
        move = input()
        while move not in self.actions:
            print( "I don't understand that. You can " + str(self.actions) )
            move = input()
        return move
    
    # Execute the desired action
    def do_action(self, action, opponent):
        if action not in self.actions:
            print("You can't do that")
        else:
            if action == "attack":
                damage = self.companion.attack()
                opponent.subtract_hp(damage)
                opponent.status()

   
            
  
