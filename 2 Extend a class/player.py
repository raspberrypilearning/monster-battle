from monster import Monster

# Player is a subclass of Monster
class Player(Monster):

    def __init__(self, monster_name):
        super().__init__(monster_name)
        self.defending = False

    # New defence methods
    def defend(self):
        self.defending = True

    def reset_defence(self):
        self.defending = False

    def is_defending(self):
        return self.defending

    # Override the subtract_hp method for a Player to allow
    # the player to defend (a Monster cannot defend)
    def subtract_hp(self, hit_amount):
        if self.defending == True:
            # Calculate max defence
            if (hit_amount - 10) < 0:
                hit_amount = 0
            else:
                hit_amount = hit_amount - 10
            print("Defended 10HP! Hit for " + str(hit_amount) + "HP")
        # Deduct the hit
        self.hp = self.hp - hit_amount
