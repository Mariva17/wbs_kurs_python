"""
Properties

"""

class Person:
    """
    pythonische Variante: Default set- und get Zugriff ist
    von außen über das Instanzattribbut selbst.

    Was iat aber mit der Business-Regel age > 0?

    @properties
    """
    def __init__(self, name, alter, nickname="default nickname") -> None:
        self.name = name
        self.age = alter  # ruft intern age.setter()
        self._nickname = nickname

    @property
    def nickname(self):
        """Read only property, da kein Setter vorhanden ist."""
        return self._nickname


    @property
    def age(self):
        """das hier ist der getter."""
        return self._age

    @age.setter
    def age(self, age):
        """das hier ist der setter. Der Getter wird dazu benötigt."""
        if age < 1:
            raise ValueError("Alter darf nicht negativ sein!")
        self._age = age


alice = Person("Alice", 14)
# alice.name = "Alice again"
alice.age = 15
# alice._age = 17  # Lass die Finger davon, nicht machen, weil _-Präfix immer bedeutet: privat
print("neues Alter:", alice.age) 
# alice.nickname = "Alice15"
print(alice.__dict__)

