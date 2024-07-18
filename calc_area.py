import abc
import math


class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round((math.pi * self.radius ** 2), 2)


class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def can_be_triangle(self):
        flag = True
        if self.side1 + self.side2 <= self.side3:
            flag = False
        elif self.side1 + self.side3 <= self.side2:
            flag = False
        elif self.side2 + self.side3 <= self.side1:
            flag = False
        return flag

    def area(self):
        if self.can_be_triangle():
            s = (self.side1 + self.side2 + self.side3) / 2
            area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
            return area
        else:
            ValueError('Sides cannot form a triangle ')

    def is_rectangular(self):
        sides = [self.side1, self.side2, self.side3]
        max_side = max(sides)
        sides.pop(max_side)
        return max_side ** 2 == sides[0] ** 2 + sides[1] ** 2
