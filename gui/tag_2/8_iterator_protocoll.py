"""
Iterator-Protocoll

__iter__ => liefert das Objekt, dass eine __next__-Methode implementiert (Iterator)
"""

# values = [1, 2, 3]
# for value in values:
#     print(value)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r},{self.age!r})"


class Kurs:
    def __init__(self, name):
        self.name = name
        self.teilnehmer = []
        self.pos = 0

    def add(self, person: Person):
        self.teilnehmer.append(person)


    def __iter__(self):
        return self


    def __next__(self):
        """Wenn diese Methode implementiert ist, ist die Klasse ein Iterator"""
        try:
            val = self.teilnehmer[self.pos]
        except IndexError:
            raise StopIteration()
        self.pos += 1
        return val


kurs = Kurs("python Kurs WBS")
bob = Person("Bob", 25)
alice = Person("Alice", 36)
kurs.add(bob)
kurs.add(alice)
#print(kurs)

# kurs_iterator = iter(kurs)
# print(next(kurs_iterator))


for teilnehmer in kurs:
    print(teilnehmer)