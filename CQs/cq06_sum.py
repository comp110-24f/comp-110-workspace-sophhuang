"""Summing the elements of a list using different loops"""

__author__: str = "730653485"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    total: float = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    total1: float = 0.0
    for num in vals:
        total1 += num
    return total1


def f_range_sum(vals: list[float]) -> float:
    total2: float = 0.0
    for num in range(0, len(vals)):
        total2 += vals[num]
    return total2
