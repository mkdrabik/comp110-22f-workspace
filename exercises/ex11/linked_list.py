"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730554383"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns data of the Node at the given index."""
    if index < 0 or head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns highest value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        return head.data
    else:
        i: int = max(head.next)
        if head.data > i:
            i = head.data
        return i
         

def linkify(items: list[int]) -> Optional[Node]:
    """Returns a linked list with the same int values as the given list."""
    if items == []:
        return None
    else:
        n: Node = Node(items[0], linkify(items[1:]))
        return n


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales a given node by a factor."""
    if head is None:
        return None
    elif head.next is None:
        head.data *= factor
        return head
    else:
        head.data *= factor
        head.next = scale(head.next, factor)
    return head
        