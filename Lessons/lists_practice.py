"""Basic practice with lists."""

# create an empty list
my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal
# print(my_numbers)

# string analogy
# my_name: str = "" # literal
# my_name: str = str() # constructor

# adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]
# print(game_points)

# indexing with lists / subscription notation
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# modify a list by index (because lists are mutable)
game_points[1] = 72
# print(game_points)

# class_num: str = "110"  # change it to "210" goal
# class_num[0] = "2"  # can't modify strings by index because they are imutable

# Getting the length
# len(game_points)

# remove an item from a list
game_points.pop(1)
# print(game_points)


# in class given assignment
def display(list_of_int: list[int]) -> None:
    idx = 0
    while idx < len(list_of_int):
        print(list_of_int[idx])
        idx += 1


display(game_points)
