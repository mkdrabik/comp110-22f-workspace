"""Dictionary exercise assignment."""
__author__ = "730554383"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns an inverted version of the inputed dicionary where the key becomes the value and vice versa"""
    names: dict[str, str] = {}
    for i in x:
        names[x[i]] = i
    return names
