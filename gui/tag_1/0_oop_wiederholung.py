"""
OOP Wiederholung

"""

class Person:
    def __init__(self, first_name: str, last_name:str) -> None:
        print(id(self))
        self.first_name = first_name
        self.last_name = last_name


    def say_hello(self) -> None:
        print(self.first_name, self.last_name)


p = Person(first_name="Bob", last_name="Jefferson")
print(id(p))
p.say_hello()

# Alle Attribute eines Objekts einzeigen
print(vars(p))  # {'first_name': 'Bob', 'last_name': 'Jefferson'}
print(p.__dict__)  # {'first_name': 'Bob', 'last_name': 'Jefferson'}




