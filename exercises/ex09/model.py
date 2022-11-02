"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730554383"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculates distance between two points."""
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Updates location of a cell."""
        self.location = self.location.add(self.direction)  
        if self.is_infected():
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():        
            return "green"
        return "null"

    def contract_disease(self) -> None:
        """Gives cell an infection."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determines if a cell is vulnerable or not."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False

    def is_infected(self) -> bool:
        """Determines if a cell is infected or not."""
        if self.sickness >= constants.INFECTED and self.sickness < constants.RECOVERY_PERIOD:
            return True
        return False

    def contact_with(self, other: Cell) -> None:
        """Updates cell if infection is present."""
        if self.is_infected() and other.is_vulnerable() and not other.is_immune():
            other.contract_disease()
        elif self.is_vulnerable and not self.is_immune() and other.is_infected():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Gives cell immunity attribute."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns true if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_infected: int, num_immune=0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        
        if len(self.population) <= num_infected + num_immune or num_infected <= 0:
            raise ValueError("Number of infected and immune cells must be lower than total number of cells and infected cells must be greater than one!!")

        for i in range(num_infected):
            self.population[i].contract_disease()

        if len(self.population) <= num_immune + num_infected or num_immune < 0:
            raise ValueError("Number of infected and immune must be lower than total number of cells and immune cells cannot be less than zero!!")

        v: int = num_infected
        for _ in range(num_immune):
            self.population[v].immunize()
            v += 1
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0

        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks distances between two cells."""
        i: int = 0
        while i < len(self.population):
            v: int = i + 1
            while v < len(self.population):
                if self.population[i].location.distance(self.population[v].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[v])
                v += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True