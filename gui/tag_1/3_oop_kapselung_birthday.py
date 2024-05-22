"""
Getter mit Sinn

"""
class Person:

    def __init__(self, name, geburtstag) -> None:
            self.name = name
            self.birthday = geburtstag

       

    @property
    def age(self):
        """hier wird auf Basis des Geburtstags das Alter errechnet
        und zurückgegeben."""
        return 13  # Berechne Alter aus self._birthday

    @property
    def birthday(self):
        return self._birtday


    @birthday.setter
    def birthday(self, geburtstag):
        # hier prüfen, ob Geburtstag valive!
        self._birtday = geburtstag


alice = Person("Alice", "12.10.1990")
print(alice.age)
# alice.name = "Alice again"
# alice.age = 15
# alice._age = 17  # Lass die Finger davon, nicht machen, weil _-Präfix immer bedeutet: privat
# print("neues Alter:", alice.age) 
# alice.nickname = "Alice15"
# print(alice.__dict__)
