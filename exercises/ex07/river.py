"""File to define River class."""

__author__ = "730653485"
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Contains all the methods and information about the ecosystem living in the river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Kills off old fish and bears."""
        # the new lists that will contain the fish/bears still within age
        new_fish: list[Fish] = []
        new_bear: list[Bear] = []
        for elem in self.fish:
            # loop through all the fish in the list
            if elem.age <= 3:
                # add the fish within the age range to the new list rather than remove the fish that are older than 3
                new_fish.append(elem)
        for elem in self.bears:
            # same thing as the loop for fish above
            if elem.age <= 5:
                new_bear.append(elem)
        # now I have to set the current list of animals to the ones that still survived
        self.fish = new_fish
        self.bears = new_bear
        return None

    def bears_eating(self):
        """Adjusts the fish numbers and hunger of bear if they ate fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # if there's at least 5 fish in the river
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Kills off starving bears."""
        new_bear: list[Bear] = []
        for bear in self.bears:
            # loop through the bears in the bear list within the Rivers class to see if any of their hunger scores go negative. Rather than removing, I will only add the bears to the new list of bears if their hunger score is 0 or higher.
            if bear.hunger_score >= 0:
                new_bear.append(bear)
        self.bears = new_bear
        return None

    def repopulate_fish(self):
        """Adjusts for fish offspring."""
        num_fish: int = len(self.fish)
        if num_fish % 2 == 0:
            num_new_fish: int = int((num_fish / 2) * 4)
            for x in range(0, num_new_fish):
                self.fish.append(Fish())
        if num_fish % 2 == 1:
            num_new_fish: int = int(((num_fish - 1) / 2) * 4)
            for x in range(0, num_new_fish):
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adjusts for bear offspring."""
        num_bears: int = len(self.bears)
        if num_bears % 2 == 0:
            # working with a population of even number of bears
            num_new_bears: int = int(num_bears / 2)
            for x in range(0, num_new_bears):
                # this for in range loop will go through the amount of new bears and keep adding that amount of bears to the list\
                self.bears.append(Bear())
                # this will initialize a new Bear instance for each new bear within the list "bears"
        if num_bears % 2 == 1:
            # working with a population of odd number of bears
            num_new_bears: int = int((num_bears - 1) / 2)
            for x in range(0, num_new_bears):
                self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints out a report of the river population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Gives a full week's report of the river population."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes _ amount of fish from the river."""
        new_fish: list[Fish] = []
        for idx in range(amount, len(self.fish)):
            new_fish.append(self.fish[idx])
        self.fish = new_fish
