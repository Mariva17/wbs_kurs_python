"""
Auto Beispiel
"""


class Car:
    def __init__(self, name) -> None:
        self.name = name

    def fahren(self) -> None:
        print(f"generisches Auto {self.name} fährt")



class Ferrari(Car):
    
    def fahren(self) -> None:
        print(f"{self.name} rast den Highway entlang")


class California(Ferrari):
    pass




# car = Car("Standardauto")
# car.fahren()

ferrari = Ferrari("Ferrari")
ferrari.fahren()


california = California("California")
california.fahren()


# Ausgabe
# print(vars(ferrari))
# print(dir(ferrari))