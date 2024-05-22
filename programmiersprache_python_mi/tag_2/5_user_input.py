"""
User-Input und Typecasting von Strings nach int/float

"""

wert = "3"
print(type(wert))

# wert = wert + 5
numeric_value = int(wert)
print(numeric_value)

float_value = float("2.2")

# EDV: EVA Eingabe, Verarbeitung, Ausgabe
# Beispiel: Berechnung der Fläche eines Rechtecks
print("Hallo User! Willkommen!")
a = input("Bitte gebe eine Zahl für Seite a ein: ") 
b = input("Bitte gebe eine Zahl für Seite b ein: ")

a = float(a)
b = float(b)

area = a * b
print("Die Flache ist: ", area)
