"""(Leicht)
Personenobjekte sollen die Operatoren für den arithetischen Vergleich
überladen.

Zwei Personen sind gleich, wenn sie gleich alt sind.

alice = Person(name="Alice", age=30)
bob = Person(name="Bob", age=30)
mallory = Person(name="Mallory", age=89)

alice > Bob # false
alice == Bob # true
alice != Bob # false
alice < mallory # true
alice >= mallory # false

Überlade die Operatoren und nutze Typehints in den Methoden.
"""
from __future__ import annotations

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, alter):
        if alter > 0 and isinstance(alter, int):
            self._age = alter
        else:
            raise ValueError("Alter darf nicht negativ sein!")


    def __eq__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age == other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __gt__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age > other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __ge__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age >= other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __lt__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age < other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __le__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age <= other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")

    def __ne__(self, other: Person) -> bool:
        if isinstance(other, Person):
            return self.age != other.age
        raise NotImplemented("Diese Operation ist nicht implementiert")
    


alice = Person(name="Alice", age=30)
bob = Person(name="Bob", age=30)
mallory = Person(name="Mallory", age=89)

print(alice > bob)
print(alice == bob)
print(alice != bob)
print(alice < mallory)
print(bob > mallory)
print(mallory >= bob)

