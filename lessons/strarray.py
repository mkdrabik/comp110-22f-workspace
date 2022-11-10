""""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union 


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for i in self.items:
                result.items.append(i + rhs)
        else: 
            assert len(self.items) == len(rhs.items)
            for v in range(len(self.items)):
                result.items.append(f"{self.items[v]}{rhs.items[v]}")
        return result

            

    


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + ", " + b)