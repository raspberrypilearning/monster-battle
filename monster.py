import random

class Monster():
    
    # Constructor
    def __init__(self):
        self.name = self.choose_name()
        self.hp = 30
        self.alive = True
        
    # Getters
    def get_name(self):
        return self.name.title()
    
    def get_hp(self):
        return self.hp
    
    def subtract_hp(self, hit):
        self.hp = self.hp - hit
        if self.hp <= 0:
            self.alive = False

    def status(self):
        print(self.get_name() + " has " + str(self.hp) + "HP")
        if not self.alive:
            print(self.get_name() + " died :(")
            self.alive = False

    def is_alive(self):
        return self.alive

    # Useful methods
    def choose_name(self):
        name_bits = ["thunder", "monster", "laser", "foot", "wing", "death", "grumble", "pants", "nibble", "moon"]
        chosen_name = random.choice(name_bits) + random.choice(name_bits)
        return chosen_name

    def attack(self):
        # Does a basic damage attack
        print( ">>> You claw your opponent for 10HP")
        return 10


    def fight(self, player):
        damage = random.choice([30, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10])
        print(">>> " + self.name + " claws you for " + str(damage) +"HP" )
        player.get_companion().subtract_hp(damage)
        player.get_companion().status()
