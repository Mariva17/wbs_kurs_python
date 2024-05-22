"""
Statische Methode

"""
class Person:
    def __init__(self, name, size):
        self.name = name
        self.size = size


    @staticmethod
    def cm_to_meter(cm) -> float:
        return cm / 100


p = Person("Bob", 180)
result = Person.cm_to_meter(180)
print(result)


## Beispiel Utility-Klasse: Sammlung von Mathe-Methoden

class MathUtill:
    """Utility-Klassen"""
    @staticmethod
    def add(x, y):
        return x + y


result = MathUtill.add(32, 74)
