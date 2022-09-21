"""Unit testing exercise."""
__author__ = "730554383"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints returns a new list of only even values."""
    nlist: list[int] = list()
    
    if len(xs) == 0:
        return nlist

    i: int = 0

    while i < len(xs):
        if xs[i] % 2 == 0:
            nlist.append(xs[i])
        i += 1
    return nlist

    
def concat(xs: list[int], xy: list[int]) -> list[int]:
    """Given two lists of ints returns a new list made of the values of both lists."""
    nlist: list[int] = list()
    i: int = 0
    
    if len(xs) > 0: 
        while i < len(xs):
            nlist.append(xs[i])
            i += 1 
    
    i = 0

    if len(xy) > 0:
        while i < len(xy):
            nlist.append(xy[i])
            i += 1
    return nlist


def sub(xs: list[int], low: int, high: int) -> list[int]:
    """Given a list, returns a new list based on the parameters inputed."""
    nlist: list[int] = list()
    if len(xs) == 0 or low > len(xs) or high <= 0:
        return nlist

    i: int = low

    if i < 0:
        i = 0

    while i < len(xs) and i < high:
        nlist.append(xs[i])
        i += 1
    return nlist