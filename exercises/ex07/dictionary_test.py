"""Dictionary testing."""
__author__ = "730554383"

from dictionary import invert
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