"""
Protokolle in Python (typing.Protocol)

"""

from typing import Protocol
import math



class Drawable(Protocol):
    def draw(self) -> None: ...
        

    def area(self) -> float: ...
        


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def draw(self) -> None:
        print("circle is drawing")


def print_shape(shape: Drawable):
    print(shape.area())
    print(shape.draw())


c = Circle(2)
print_shape(c)