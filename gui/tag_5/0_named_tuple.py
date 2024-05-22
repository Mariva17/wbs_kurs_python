"""
NamedTuple. Zum Halten von unverändlichen Daten.
Dieser NamedTuple unterstützt die Datentypen.
"""
from typing import NamedTuple


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


v1 = Vector(1, 2, 3)
v1.x = 4
print(v1)

print("*" * 40)

class VectorNeu(NamedTuple):
    """Neue Implementierung von Vector. Unveränderlich, da Tuple."""

    x: int
    y: int
    z: float


v2 = VectorNeu(4, 5, 6)
print(v2.__repr__())
print(type(v2), v2[0], v2.x)
#print(dir(v2))
print(v2._asdict())  # {'x': 4, 'y': 5, 'z': 6}

print("v2 ist Instanz von Tuple: ", isinstance(v2, tuple))  # True
print("v2 ist Instanz von VectorNeu: ", isinstance(v2, VectorNeu))  # True
print("Docstring von VectorNeu: ", v2.__doc__)