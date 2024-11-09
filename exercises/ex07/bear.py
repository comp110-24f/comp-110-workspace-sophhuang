"""File to define Bear class."""

__author__ = "730653485"


class Bear:
    """Contains the bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the bear's age and hunger."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Adjusts their stats by the day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Adjusts hunger score after a bear eats."""
        self.hunger_score += num_fish
