"""More list utility functions"""

__author__: str = "730653485"


def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []
    # made an empty list that I can add the even values to and return because I shouldn't mutate the original list
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 == 0:
            # this checks if the value is even due to the remainder being 0 if divisable by 2
            even_list.append(input[idx])
        idx += 1
    return even_list


def sub(input: list[int], s_idx: int, e_idx: int) -> list[int]:
    if s_idx < 0:
        s_idx = 0
        # this fixes the indexes if there are out of range
    if e_idx > len(input):
        e_idx = len(input)
    new_list: list[int] = []
    while s_idx < e_idx:
        new_list.append(input[s_idx])
        s_idx += 1
    return new_list


def add_at_index(input: list[int], num: int, idx: int) -> None:
    if idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # append something to the end of the list
    i = len(input) - 1
    while i > idx:
        # this runs through everything before the idx I want to change and moves them one to the right
        input[i] = input[i - 1]
        i -= 1
    input[idx] = num
    # this adds the value I want to add at the index I want to add it to.
