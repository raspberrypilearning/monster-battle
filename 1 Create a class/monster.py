import random

class Monster():

    # Constructor
    def __init__(self, monster_name):
        self.name = monster_name.title()
        self.hp = 30
        self.alive = True

    # Getters and setters
    def get_name(self):
        return self.name

    def describe(self):
        print("[" + self.name +"] has " + str(self.hp) + "HP")

    def is_alive(self):
        return self.alive

    def subtract_hp(self, hit):
        self.hp = self.hp - hit
        if self.hp <= 0:
            self.alive = False

    def attack(self, monster):
        damage = random.choice([30, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10])
        print(">>> " + self.name + " hits " + monster.get_name() + " for " + str(damage) +"HP" )
        monster.subtract_hp(damage)
