"""List Utility function exercise"""

__author__: str = "730653485"


def all(list: list[int], num: int) -> bool:
    idx: int = 0
    # after a good amount of troubleshooting, I've changed the order of returning False and True, and having the index increase at the end so when I reach the last index of the list and if established that it equals the integer inputted, I can immediately return True and exit the function body
    while idx < len(list):
        if num != list[idx]:
            return False
        if idx == len(list) - 1:
            # have to put "-1" because index starts at 0
            return True
        elif num == list[idx]:
            idx += 1


def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    if len(list) != 0:
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
        if idx == len(list1) - 1:
            return True
        if list1[idx] == list2[idx]:
            idx += 1


def extend(list1: list[int], list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):
        # less than length of list2 because that's the list we're going through the index of to add the numbers onto list1
        list1.append(list2[idx])
        idx += 1
