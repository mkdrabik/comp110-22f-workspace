"""Dictionary testing."""
__author__ = "730554383"

from dictionary import invert


def test_is_inverted() -> None:
    """Tests to ensure the function works with a normal argument."""
    xs: dict[str, str] = {"Mason": "Drabik", "Kris": "Jordan", "Michael": "Jordan"}
    assert invert(xs) == {"Drabik": "Mason", "Jordan": "Kris", "Jordan": "Michael"}

def test_empty_dictionary() -> None:
    """Tests to ensure the function works with an empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_one_key() -> None:
    """Tests to ensure that the function works when dict has only one key."""
    xs: dict[str, str] = {"Mason": "Drabik"}
    assert invert(xs) == {"Drabik": "Mason"}