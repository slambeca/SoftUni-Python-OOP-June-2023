from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def calculate_area(self):
        return self.base * self.height / 2


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Circle(10), Triangle(10, 5)]
calculator = AreaCalculator(shapes)
print("The total area is:", f"{calculator.total_area:.2f}")
# The total area is: 351.16