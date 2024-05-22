"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an. (MITTEL)

# Es gelten folgende Constraints (Regeln):
- Der Name muss mindestens drei Zeichen lang sein
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock haben".
- Im Fehlerfall raise ValueError.

Implementiere auch __str__ und __repr__.

Teste mit folgenden Produkten:
products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern
    ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
    ("Za", 23.2, "in stock"),  # muss scheitern.
]
Nutze zum testen einen Loop und try-except
"""

class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit

    # Getter-Methode für name
    @property
    def name(self):
        return self._name

    
   
    # Setter-Methode für name
    @name.setter
    def name(self, name):
        if len(name) >= 3:
            self._name = name
        else:
            raise ValueError ("Name darf laenge sein!")

    # Getter-Methode für preis
    @property
    def preis(self):
        return self._preis

    # Setter-Methode für preis
    @preis.setter
    def preis(self, preis):
        
        if not all(
            [isinstance(preis, (float, int)),
            preis >= 0]):
            raise ValueError("Ungültiger Preis")
        else:
            self._preis = preis

    # Getter-Methode für verfuegbarkeit
    @property
    def verfuegbarkeit(self):
        return self._verfuegbarkeit


    # Setter-Methode für verfuegbarkeit
    @verfuegbarkeit.setter
    def verfuegbarkeit(self, verfuegbarkeit):
        if verfuegbarkeit not in ["in stock", "out of stock"]:
            raise ValueError("Ungültige verfuegbarkeit")
        self._verfuegbarkeit = verfuegbarkeit



    def __str__(self) -> str: 
        return self.name


def test(products):
    for product in products:
        try:
            p = Produkt(*product)
        except ValueError as e:
            print(e, product)
        else:
            print(f"{p} ist ein gültiges Produkt.")   



if __name__ == "__main__":

    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
        ("Za", 23.2, "in stock"),  # muss scheitern.
    ]

    test(products)


