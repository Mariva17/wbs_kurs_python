"""
Methoden-Polymorphie

"""

class Tier:
    def sound(self):
        print("Tier macht sound")


class Hund(Tier):
    def sound(self):
        print("Bund bellt")


class Ente(Tier):
    def sound(self):
        print("Ente quackt")


class Elephant(Tier):
    pass


animals = [Tier(), Hund(), Ente(), Elephant()]
for animal in animals:
    animal.sound()
