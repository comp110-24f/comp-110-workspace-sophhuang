"""File to define Fish class."""

__author__ = "730653485"


class Fish:
    """Contains the fish."""

    age: int

    def __init__(self):
        """Initializes the fish's age."""
        self.age = 0

    def one_day(self):
        """Adjusts age as a day passes."""
        self.age += 1
        return None
