class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Student(Person):
    def __init__(self, name, age, nr):
        super().__init__(name, age)
        self.nr = nr


    def __str__(self) -> str:
        return f"{self.name} hat Matrikelnummer {self.nr} und ist {self.age} alt."

p = Person(name="Bob", age=25)
s = Student(name="Alice", age=22, nr = "235417a")
print(s)