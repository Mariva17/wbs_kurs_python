"""(leicht)
Aufgabe:
Erstelle eine Klasse Vektor, die eine Klassen-Methode implementiert.
die Klassen-Methode heisst from_dict und erstellt ein Vector-Objekt
auf Basis eines Dict in der Form:

d = {
    "x_point": 2,
    "y_point": 10,
}

oder

d = {
    "y_point": 11,
    "x_point": 3,
}

Zudem soll die Klasse die __repr__() - Methode implementieren

>>> v2 = Vector.from_dict(d)
>>> print(v2)
Vector(11, 3)
>>> print(type(v2))
<class '__main__.Vector'>


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
"""

from __future__ import annotations

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    @classmethod
    def from_dict(cls, csv_dict: dict[str, int]):
        # res = [val for val in csv_dict.values()]
        # return cls(res[0], res[1])

        x, y = csv_dict["x_point"], csv_dict["y_point"]
        if type(x) is int and type(y) is int:
            return cls(x, y)
        else:
            raise TypeError("Der Vector benötigt ganzzahlige Werte!")


    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.x!r},{self.y!r})"

        



d = {
    "x_point": 2,
    "y_point": 10,
}

d2 = {
    "y_point": 11,
    "x_point": 3,
}

v1 = Vector.from_dict(d)
print(v1)

v2 = Vector.from_dict(d2)
print(v2)
print(type(v2))

