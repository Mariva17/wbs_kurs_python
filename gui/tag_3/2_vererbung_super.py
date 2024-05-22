"""
Basisklasse Rectangle
Kindklasse Square

super() bietet Zugriff auf die Superklasse (via einem Proxy-Objekt)
"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self) -> float:
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
        print("area inner: ", super().area)

r = Rectangle(a=2, b=4)
print("Größe des Rechtecks: ", r.area)

s = Square(a=3)
print("Größe des Squares: ", s.area)


