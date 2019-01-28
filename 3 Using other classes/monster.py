import random
from time import sleep
from item import Item

class Monster():

    def __init__(self, monster_name):
        self.name = monster_name
        self.hp = 30

        # Add the item attribute which creates an Item object
        self.item = Item()

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

    # Add the describe item method
    def describe_item(self):
        print(self.item)

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def subtract_hp(self, hit_amount):
        self.hp = self.hp - hit_amount

    # Change the implementation of attack so that it attacks using the item's attack value
    def attack(self, target):
        print(">>> " + self.name + " hits " + target.get_name() + " for " + str(self.item.get_attack_value()) +"HP" )
        target.subtract_hp(self.item.get_attack_value())
