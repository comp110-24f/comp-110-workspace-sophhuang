__author__ = "730653485"

from CQs.cq07.find_max import find_and_remove_max


def test_max_return() -> None:
    fav_nums: list[int] = [9, 5, 24, 10]
    assert find_and_remove_max(fav_nums) == 24


def test_max_mutate() -> None:
    fav_nums: list[int] = [9, 5, 24, 10]
    find_and_remove_max(fav_nums)
    assert fav_nums == [9, 5, 10]


def test_max_edge() -> None:
    input: list[int] = []
    assert find_and_remove_max(input) == -1
