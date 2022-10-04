"""Dictionary exercise assignment."""
__author__ = "730554383"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns an inverted version of the inputed dicionary where the key becomes the value and vice versa"""
    names: dict[str, str] = {}
    vals: list[str] = list()
    i: int = 0
    v: int = 0
    for y in x:
        vals.append(x[y])
    
    while i < len(vals):
        v = i + 1
        while v < len(vals):
            if vals[i] == vals[v]:
                raise KeyError
            v += 1
        i += 1
    
    for i in x:
        names[x[i]] = i
    return names



    



