from monster import Monster

# Player is a subclass of Monster
class Player(Monster):

    def __init__(self, monster_name):
        super().__init__(monster_name)
        self.defending = False
        self.hp = 40    # Make a player start on a higher HP level

    # New defence methods
    def defend(self):
        self.defending = True

    # Override the subtract_hp method for a Player to allow
    # the player to defend (a Monster cannot defend)
    def subtract_hp(self, hit_amount):
        if self.defending == True:
            print("Defended 10HP of damage!")
            hit_amount = hit_amount - 10
            if hit_amount < 0:
                hit_amount = 0

            self.defending = False  # Reset defence

        # Deduct the hit
        self.hp = self.hp - hit_amount
