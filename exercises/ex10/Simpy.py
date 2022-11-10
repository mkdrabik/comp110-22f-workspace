"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, vals: list[float]) -> None:
        """Constructs a new Simpy object."""
        self.values = vals

    def __repr__(self) -> str:
        """Creates a string representation of Simpy."""
        return f"Simpy({self.values})"
        
    def fill(self, val: float, quant: int) -> None:
        """Fills the Simpy's values with a float based on times the int specifies."""
        self.values = []
        for _ in range(quant):
            self.values.append(val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Adds values in a range based on the step to the list."""
        assert step != 0.0
        i: float = start
        if step > 0:
            while i < stop:
                self.values.append(i)
                i += step
        else:
            while i > stop:
                self.values.append(i)
                i += step
    
    def sum(self) -> float:
        """Returns the sum of all the values in the simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new simpy object that is the result of the two parameters being added."""
        vals: list[int] = []    
        if isinstance(rhs, float):
            for v in self.values:
                vals.append(v + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                vals.append(self.values[i] + rhs.values[i])
                i += 1
        
        fin: Simpy = Simpy(vals)

        return fin

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new simpy object that is the result of the two parameters being added."""
        vals: list[int] = []    
        if isinstance(rhs, float):
            for v in self.values:
                vals.append(v ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                vals.append(self.values[i] ** rhs.values[i])
                i += 1
        
        fin: Simpy = Simpy(vals)

        return fin
  
        
