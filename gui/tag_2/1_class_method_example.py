"""

Class - Method Decorator.

Fabrikmethode

With __future__ module's inclusion, you can slowly be accustomed to incompatible 
changes or to such ones introducing new keywords.

"""
from __future__ import annotations

class Pizza:
    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients

    @classmethod
    def example(cls): 
        print("Klasse: ", cls)


    def show_ingredients(self):
        print(self.ingredients)
        print(self)

    @classmethod
    def salami(cls) -> Pizza:
        return cls(["mozarella", "Salami", "Basilikum"])


    @classmethod
    def margarita(cls) -> Pizza:
        return cls(["mozarella", "Basilikum"])


    @classmethod
    def from_csv_string(cls, csv_string: str):
        # Salami, Basilikum
        return cls(csv_string.split(","))


    def __str__(self) -> str:
        return "Pizza mit: " + ",".join(self.ingredients)


pizza_salami = Pizza(["mozarella", "Salami", "Basilikum"]) # klassisch
pizza_salami.show_ingredients()
pizza_salami.example() # Klassenmethode über Objekt aufrufen
Pizza.example()

pizza_salam_neu = Pizza.salami() # über classmethod-Fabrik
pizza_2 = Pizza.from_csv_string("Salami, Peperoni, Pilze")
print(pizza_2)
