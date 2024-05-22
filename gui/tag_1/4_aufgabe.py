"""

Erstelle eine Klasse Rechteck mit den Attributen breite und hoehe.
Die Klasse benötigt eine Methode area, die die Fläche ausrechnet und zurückgibt.

breite darf nicht < 0 sein: ValueError
hoehe darf nicht < 0 sein: ValueError

r1 = Rechteck(breite=10, hoehe=13)
r1.hoehe = 3
print(r1.area()) # 30

r1.hoehe = -12 # ValueError
r2 = Rechteck(breite=10, hoehe=-1)
ValueError!

"""


class Rechteck:
    def __init__(self, breite, hoehe) -> None:
        self.breite = breite
        self.hoehe = hoehe


    @property
    def breite(self):
        return self._breite


    @breite.setter
    def breite(self, breite):
        if breite <= 0:
            raise ValueError("Breite darf nicht negativ sein!")
        self._breite = breite


    @property
    def hoehe(self):
        return self._hoehe



    @hoehe.setter
    def hoehe(self, hoehe):
        if hoehe <= 0:
            raise ValueError("Hoehe darf nicht negativ sein!")
        self._hoehe = hoehe

    @property
    def area(self):
        return self.breite * self.hoehe


    def area_func(self):
        """Area nochmal als Methode implementiert"""
        return self.breite * self.hoehe



if __name__ == "__main__":
    r1 = Rechteck(breite=10, hoehe=13)
    r1.hoehe = 1
    print("Area von Rechteck: ", r1.area)
    print("Area von Rechteck: ", r1.area_func())

    # r2 = Rechteck(-10, 10)
    # print(r2.area())

    # selbst definierten Attribute des Objekts ausgeben via __dict__ ODER vars()
    print(r1.__dict__)
    print(vars(r1))

    # zeige alle Attribute und Methoden eines Objekt an
    print(dir(r1))
