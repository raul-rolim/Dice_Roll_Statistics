import random as rng

class Die:

    def __init__(self, die_sides=6):
        self.die_sides = die_sides

    def roll(self):
        return rng.randint(1, self.die_sides)