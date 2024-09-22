"""Calculates the tea bags, treats, and total cost needed for a cozy tea party"""

__author__: str = "730653485"


def main_planner(guests: int) -> None:
    """The entrypoint of my program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # At first while reading the instructions, I didn't quite conceptualize that when writing the print code, I had to write the string of words that came before the number printed. After running the program once in Trailhead, I saw my result was not identical to the image provided in the instructions and quickly I had forgotten to include the coding for the other words such as "A Cozy Tea Party for __ People!"
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # I had to complete some problem-solving to write the cost() function call line above to figure out how to write that the tea and treat number was the return of the functions tea_bags and treat_count. I took the longest to determine the parameter people would be equal to the argument guests.


def tea_bags(people: int) -> int:
    """Calculates the amount of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the amount of treats needed based on the amount of tea gustes are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)
    # since 1.5 is a float, I realized that it didn't match the return type of int. I used the int() function to make it the right return type.


def cost(tea_count: int, treat_count: int) -> float:
    """computes the cost of the tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
