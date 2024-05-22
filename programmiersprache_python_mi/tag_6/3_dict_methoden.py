"""
Methoden von Datentyp dicts

"""
from pprint import pprint

capitals = {
    "Hessen": "Wiesbaden",
    "Saarland": "Saarbrücken",
    "Baden-Württemberg": "Stuttgart",
    "Rheinland-Pfalz": "Mainz",
    "Nordrhein-Westfalen": "Düsseldorf",
}

# pop: Element an Key rauspoppen und Wert zurückgeben
city = capitals.pop("Hessen", "nicht vorhanden")
print(city)

# Löscht das zuletzt hinzugefügte
city = capitals.popitem()
print(city) # ('Nordrhein-Westfalen', 'Düsseldorf')

# Ein Dict updaten
capitals["Sachsen"] = "Dresden"
pprint(capitals, width=1)

#Ein Dict update mit update - Methode
new_capitals = {
    "Berlin": "Berlin",
    "Brandenburg": "Postdam"
}
capitals.update(new_capitals)
pprint(capitals)

capitals.copy() # flache Kopie

