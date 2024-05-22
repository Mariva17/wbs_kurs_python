"""
Operator Overloading
"""

from __future__ import annotations

class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    @property
    def area(self):
        return self.breite * self.hoehe


    def __eq__(self, other: Rechteck) -> bool:
        if isinstance(other, Rechteck):
            return self.area == other.area

        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __add__(self, other: Rechteck) -> Rechteck:
        if isinstance(other, Rechteck):
            neue_breite = self.breite + other.breite
            neue_hoehe = self.hoehe + other.hoehe
            r = Rechteck(neue_breite, neue_hoehe)
            return r
        raise NotImplemented("Diese Operation ist nicht implementiert")


a = Rechteck(10, 20)
b = Rechteck(20, 10)
print(a == b)  # prüft, ob Flächen gleich sind
print(a + b) # erzeugt neues Rechteck


# a == b => a.__eq_(b) soll gleich sein, wenn Fläche gleich ist
# a + b => __add__