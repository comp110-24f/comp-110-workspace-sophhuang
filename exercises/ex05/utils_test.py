"""Testing the list utility functions"""

__author__: str = "730653485"

from exercises.ex05.utils import only_evens, sub, add_at_index


# test for only_evens
def test_return_only_evens() -> None:
    """tests for correct return"""
    lst: list[int] = [1, 2, 3, 4]
    assert only_evens(lst) == [2, 4]


def test_mutate_only_evens() -> None:
    """tests for no mutation of the list"""
    lst: list[int] = [1, 2, 3, 4]
    only_evens(lst)
    assert lst == [1, 2, 3, 4]


def test_edge_only_evens() -> None:
    "tests for how it handles an empty list"
    lst: list[int] = []
    assert only_evens(lst) == []


# test for sub
def test_return_sub() -> None:
    """tests for correct return"""
    lst: list[int] = [1, 5, 7, 3, 6]
    assert sub(lst, 1, 3) == [5, 7]


def test_mutate_sub() -> None:
    """tests for no mutation of the list"""
    lst: list[int] = [1, 5, 7, 3]
    sub(lst, 1, 3)
    assert lst == [1, 5, 7, 3]


def test_edge_sub() -> None:
    """tests how the function handles index out of range"""
    lst: list[int] = [1, 5, 7, 3]
    assert sub(lst, -2, 8) == [1, 5, 7, 3]


# test of add_at_index
def test_return_add_at_index() -> None:
    """test for correct return"""
    lst: list[int] = [1, 2, 10]
    assert add_at_index(lst, 4, 2) == None


def test_mutate_add_at_index() -> None:
    """test for mutation of list"""
    lst: list[int] = [1, 2, 10]
    add_at_index(lst, 4, 2)
    assert lst == [1, 2, 4, 10]


import pytest


def test_edge_add_at_index() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 10], 3, 20)
