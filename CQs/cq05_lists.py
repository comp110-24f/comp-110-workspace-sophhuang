"""Mutating functions"""

__author__ = "730653485"


def manual_append(list: list[int], num: int) -> None:
    list.append(num)


def double(list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):
        list2[idx] = list2[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
