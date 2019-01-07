import random
from time import sleep
class Monster():

    # Constructor
    def __init__(self, monster_name):
        self.name = monster_name
        self.hp = 30

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_hp(self):
        return self.hp

    def set_hp(self, hp_amount):
        self.hp = hp_amount

    def describe(self):
        print("[" + self.name +"] has " + str(self.hp) + "HP")
        sleep(3)

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def subtract_hp(self, hit_amount):
        self.hp = self.hp - hit_amount

    def attack(self, target):
        damage = random.choice([30, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10])
        print(">>> " + self.name + " hits " + target.get_name() + " for " + str(damage) +"HP" )
        target.subtract_hp(damage)
