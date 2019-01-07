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
    """Prints the monster's name and HP and then waits 3 seconds (no return value)"""
    pass

  def is_alive(self):
    """Returns True if the monster is alive and False if not"""
    pass

  def subtract_hp(self, hit_amount):
    """Subtracts the hit_amount from this monster's HP (no return value)"""
    pass

  def attack(self, target):
    """Chooses a random number for the amount of damage, subtracts that
    number from the target's HP and prints a message saying what happened
    (no return value)"""
    pass
