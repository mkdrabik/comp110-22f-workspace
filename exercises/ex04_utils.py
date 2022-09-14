"""Working with lists!!!"""
__author__ = "730554383"


def all(numbers: list[int], num: int) -> bool:
    """Transverses a list and returns if all the ints in the list are the same as the given."""
    if len(numbers) == 0:
        return False
    i: int = 0
    same: bool = True

    while i < len(numbers) - 1:
        if numbers[i] == num:
            i += 1
        else:
            same = False
            i = len(numbers)
    return same


def max(values: list[int]) -> int:
    """Finds max value in a list."""
    if len(values) == 0:
        raise ValueError("max() arg is an empty List")

    max: int = values[0]
    ind: int = 0

    while ind < len(values):
        if max <= values[ind]:
            max = values[ind]
            ind += 1
        else:
            ind += 1
    return max


def is_equal(user_values1: list[int], user_values2: list[int]) -> bool:
    """Transverses both lists to see if each value equals each other."""
    if len(user_values1) != len(user_values2):
        return False
    v: int = 0
    equal: bool = True

    while v < len(user_values1) - 1:
        if user_values1[v] == user_values2[v]:
            v += 1 
        else:
            equal = False
            v = len(user_values1)
    return equal