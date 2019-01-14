from time import sleep

class Monster():
  def __init__(self, monster_name):
    self.name = monster_name

  # Methods
  # -----------------------------------
  def get_name(self):
    return self.name

  def set_name(self, new_name):
    self.name = new_name

  # Implement these yourself
  # -----------------------------------
  def describe(self):
    """Prints the monster's name and HP, then waits 3 seconds (no return value)"""
    pass

  def is_alive(self):
    """Returns True if the monster is on 1HP or more and False if not"""
    pass

  def subtract_hp(self, hit_amount):
    """Subtracts the hit_amount from this monster's HP (no return value)"""
    pass

  def attack(self, target):
    """Chooses a random number between 10 and 30 for the amount of damage, subtracts that
    number from the **target's** HP and prints "<monster name> got hit for <x> HP"
    The 'target' is a Monster object (so it has the exact methods implemented here)
    (no return value)

    Extra challenge: Print the message <monster name> got hit by <monster name> for <x> HP"
    """
    pass
