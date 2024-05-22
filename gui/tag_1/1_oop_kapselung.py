"""

Kapselung

"""

class PersonOld:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def set_age(self, age):
        if age < 1:
            raise ValueError("Alter darf nicht negativ sein!")
        self.age = age

    def get_age(self):
        return self.age



class Person:
    """
    pythonische Variante: Default set- und get Zugriff ist
    von außen über das Instanzattribbut selbst.

    Was iat aber mit der Business-Regel age > 0?
    """
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age



bob = PersonOld("Bob", 3)
# bob.age = 4
bob.set_age(4)  # Alter ändern über set_age()
print("neues Alter: ", bob.get_age())

## Pythonische Variante
alice = Person("Alice", 14)
alice.age = 10 # Alter ändern direkt
# alice.age = -6  # Problem: Alter wird beim Setzen nicht geprüft
print("neues Alter:", alice.age)
