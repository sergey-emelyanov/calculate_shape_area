import abc
import math


class Shape(abc.ABC):

    @abc.abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return round((math.pi * self.radius ** 2), 2)


class Triangle(Shape):

    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area, 2)

    def is_rectangular(self) -> bool:
        return self.side1 ** 2 == (self.side2 ** 2 + self.side3 ** 2) or \
               self.side2 ** 2 == (self.side1 ** 2 + self.side3 ** 2) or \
               self.side3 ** 2 == (self.side1 ** 2 + self.side2 ** 2)
