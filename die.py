from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        """Assume a six-side die"""
        self.num_sides = num_sides

    def roll(self):
        """Retrun a random value between 1 and number os sides"""
        return randint(1, self.num_sides)
        