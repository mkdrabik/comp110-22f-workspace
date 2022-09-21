"""Unit testing functons."""
__author__ = "730554383"

from utils import only_evens, concat, sub


def test_list_empty() -> None:
    """Tests to ensure that an empty list returns an empty list."""
    xs: list[int] = list()
    assert only_evens(xs) == []


def test_list_functionality() -> None:
    """Tests to ensure that the function returns a list of even values."""
    xs: list[int] = [10, 11, 12, 13]
    assert only_evens(xs) == [10, 12]


def test_list_no_evens() -> None:
    """Tests to ensure a list with no evens returns empty."""
    xs: list[int] = [11, 13, 15]
    assert only_evens(xs) == []


def test_both_lists_full() -> None:
    """Tests to make sure an empty list is returned if both are empty."""
    xs: list[int] = list()
    xy: list[int] = list()
    assert concat(xs, xy) == []


def test_one_full_one_empty() -> None: 
    """Tests that a list is formed even if one list is empty"""
    xs: list[int] = [1, 2, 3]
    xy: list[int] = list()
    assert concat(xs, xy) == [1, 2, 3]


def test_both_full() -> None:
    """Tests to see that a list is formed when both lists are full."""
    xs: list[int] = [1, 2, 3]
    xy: list[int] = [4, 5, 6]
    assert concat(xs, xy) == [1, 2, 3, 4, 5, 6]


def test_boudns() -> None:
    """Tests to see that a list is returned when the low argument is negative and high argument is higher then the length of the list."""
    xs: list[int] = [1, 2, 3]
    assert sub(xs, -1, 4) == [1, 2, 3]