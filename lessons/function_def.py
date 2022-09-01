"""An example of function definition"""

def my_max(a: int, b: int) -> int:
    """Returns largest argument"""

    if a >= b:
        return a
    
    return b

x: int = 7
y: int = 6
results: int= my_max(y, x)
print(results)