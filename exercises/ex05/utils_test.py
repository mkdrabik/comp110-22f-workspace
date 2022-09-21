"""Unit testing functons."""
__author__ = "730554383"

from utils import only_evens


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
