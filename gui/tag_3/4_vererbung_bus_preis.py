"""
mit super().fahrpreis() bekommen wir Ergebniss der Elternklassen-Methode fahrpreis()
"""


class Fahrzeug:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


    def fahrpreis(self):
        return self.capacity * 100


class Bus(Fahrzeug):
    def fahrpreis(self):
        amount = super().fahrpreis()
        amount = amount / 100
        return amount



transporter = Bus("Reisebus Mercedes", 50)
print("Busfahrpreis: ", transporter.fahrpreis())