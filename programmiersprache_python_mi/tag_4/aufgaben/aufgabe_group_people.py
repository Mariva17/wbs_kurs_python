"""
Aufgabe: Gruppen von Personen (Mittel)

Es soll eine Liste von Personen in Gruppen der Größe N aufgeteilt werden.
Überschüssige Personen sollen in der letzten Gruppe untergebracht werden.

N = 3

Nutze zum Mischen der Personen die Funktion random.shuffle.
Recherchiere dazu die Funktionsweise von random.shuffle.
"""

import random

people = [
    "Blitzkraft",
    "Stahlfalke",
    "Nachtschatten",
    "Eisfeuer",
    "Quantenmann",
    "Sternenlicht",
    "Turboflug",
    "Silberpfeil",
    "Mondgeist",
    "Phantomwind",
    "Saphirblick",
    "Donnerfaust",
]
random.shuffle(people)
print(people)

gruppe_size = 3
gruppen = [people[i:i + gruppe_size] for i in range(0, len(people), gruppe_size)]
print(gruppen)

