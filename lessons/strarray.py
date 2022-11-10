""""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union 


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        for i in self.items:
            result.items.append(i + rhs)
        return result

        

    


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")