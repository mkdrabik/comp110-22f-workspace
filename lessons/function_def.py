"""An example of function definition"""

def my_max(a: int, b: int) -> int:
    """Returns largest argument"""

    if a >= b:
        return a
    else:
        return b

results: int= my_max(10, 4)
print(results)