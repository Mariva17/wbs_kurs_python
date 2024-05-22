"""
Abstract Base Classes

"""
import math
from abc import ABC, abstractmethod
from collections.abc import Sequence

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b
    



c = Circle(2.2)
print(c.area())


r = Rectangle(3, 4)
print(r.area())


def print_areas(shapes: list[Shape]):
    for shape in shapes:
        print(shape.area())


print_areas([c, r])


class MySeq(Sequence):
    pass


# s = MySeq() Eigene Sequenz erstellen schlägt fehl, weil __getitem__ und __len__
# nicht implementiert sind