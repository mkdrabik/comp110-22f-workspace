"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int, float] = "world") -> str:
    """A delightful greeting"""
    greeting: str = "Hello " 
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int): 
        greeting += "COMP" + str(name)
    else:
        greeting += "Hi, Alien life sector "  + str(name)
    return greeting


print(hello("name"))

print(hello())

print(hello(110))

print(hello(110.0))