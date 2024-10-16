__author__ = "730653485"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    max_num: int = 0
    idx: int = 0
    while idx < len(input):
        if max_num < input[idx]:
            max_num = input[idx]
        idx += 1
    idx2: int = 0
    while idx2 < len(input):
        if input[idx2] == max_num:
            input.pop(idx2)
        else:
            idx2 += 1
    return max_num
