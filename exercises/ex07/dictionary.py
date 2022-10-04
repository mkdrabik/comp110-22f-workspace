"""Dictionary exercise assignment."""
__author__ = "730554383"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns an inverted version of the inputed dicionary where the key becomes the value and vice versa."""
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

 
def favorite_color(x: dict[str, str]) -> str:
    """Returns a the color that appears most in a given dictionary."""
    colors: list[str] = []
    nums: list[int] = []  
    i: int = 0
    v: int = 0
    count: int = 0
    max: int = 0
    
    for y in x:
        colors.append(x[y])
    
    while i < len(colors):
        while v < len(colors):
            if colors[i] == colors[v]:
                count += 1
            v += 1
        nums.append(count)
        count = 0
        v = 0
        i += 1
    
    i = 0
    max = nums[i]

    while i < len(nums):
        if max < nums[i]:
            max = nums[i]
        i += 1    
    return colors[nums.index(max)]


def count(x: list[str]) -> dict[str, int]:
    """Returns a dictionary based on how many times a string appears in a list."""
    vals: dict[str, int] = {}
    val: str = ""
    i: int = 0
    v: int = 0
    appearences: int = 0

    while i < len(x):
        val = x[i]
        v = i

        if val in vals: 
            i += 1
        else:
            while v < len(x):
                if x[i] == x[v]:
                    appearences += 1
                v += 1
            
            vals[val] = appearences
            appearences = 0
            i += 1
    return vals