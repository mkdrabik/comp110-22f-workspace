"""Dictionary testing."""
__author__ = "730554383"


from dictionary import invert, favorite_color, count
import pytest


def test_is_inverted() -> None:
    """Tests to ensure the function works with a normal argument."""
    xs: dict[str, str] = {"Mason": "Drabik", "Kris": "Jordan", "Michael": "Jeff"}
    assert invert(xs) == {"Drabik": "Mason", "Jordan": "Kris", "Jeff": "Michael"}


def test_empty_dictionary() -> None:
    """Tests to ensure the function works with an empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_one_key() -> None:
    """Tests to ensure that the function works when dict has only one key."""
    with pytest.raises(KeyError):
        xs: dict[str, str] = {"Mason": "Drabik", "Miles": "Drabik"}
        invert(xs)


def test_normal_funcationality_favorite_colors() -> None:
    """Tests to ensure normal functionality of the function."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Mason": "green"}
    assert favorite_color(xs) == "blue"


def test_two_maxes() -> None:
    """Tests to ensure that the first of the two highest counted colors appear."""
    xs: dict[str, str] = {"Mason": "blue", "Miles": "yellow", "Ciel": "yellow", "Luke": "blue"}
    assert favorite_color(xs) == "blue"


def test_one_color() -> None:
    """Tests to ensure if only one color is present that color is returned."""
    xs: dict[str, str] = {"Mason": "blue"}
    assert favorite_color(xs) == "blue"


def test_normal_input() -> None:
    """Tests to ensure function works properly with a normal input."""
    xs: list[str] = ["a", "a", "a", "b", "b", "c"]
    assert count(xs) == {"a": 3, "b": 2, "c": 1}


def test_all_equal() -> None:
    """Tests to ensure if every value is equal function still works properly."""
    xs: list[str] = ["a", "b", "c"]
    assert count(xs) == {"a": 1, "b": 1, "c": 1}


def test_empty() -> None:
    """Tests to ensure an empty dictionary is returned if list is empty."""
    xs: list[int] = []
    assert count(xs) == {}