"""List Utility function exercise"""

__author__: str = "730653485"


def all(list: list[int], num: int) -> bool:
    idx: int = 0
    if len(list) == 0:
        return False
    while idx < len(list):
        if num != list[idx]:
            # as soon as any number in the list doesn't equal the number inputted, I can return false and exit the function body
            return False
        idx += 1
    return True


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_num: int = list[idx]
    # I made max_num the local variable that I can manipulate and keep setting equal to the new maximum value in the if then block below
    while idx < len(list):
        if max_num < list[idx]:
            max_num = list[idx]
        idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):
        # less than length of list2 because that's the list we're going through the index of to add the numbers onto list1
        list1.append(list2[idx])
        idx += 1
