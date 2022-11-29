"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730554383"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_index_ob() -> None:
    """Tests to see that error is raised when index is wrong."""
    with pytest.raises(IndexError):
        linked_list = Node(1, Node(2, Node(3, None)))
        value_at(linked_list, 4)

    
def test_finds_value() -> None:
    """Tests to find value at Index."""
    assert value_at(Node(10, Node(20, Node(30, None))), 2) == 30


def test_finds_max() -> None:
    """Tests to ensure that the max value is found."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_empty() -> None:
    """Tests to ensure nothing happens when list is empty."""
    with pytest.raises(ValueError):
        max(None)


def test_links() -> None:
    """Tests to enure that the list is linked properly."""
    assert str(linkify([1, 2, 3])) == "1 -> 2 -> 3 -> None"


def test_empty_links() -> None:
    """Test to ensure none is returned if list is empty."""
    assert linkify([]) is None


def test_scale() -> None:
    """Tests to ensure scaling is done properly."""
    assert str(scale(linkify([1, 2]), 2)) == "2 -> 4 -> None"


def test_empty_scale() -> None:
    """Tests to ensure None is returned when linkfy is empty."""
    assert scale(linkify([]), 2) is None