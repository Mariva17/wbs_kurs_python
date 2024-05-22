# Lese die Datei worldcities.csv mit dem CSV - Reader ein,
# sortiere die Einträge nach dem Feld "city_ascii" (siehe worldcities.csv) und speichere sie in einer
# neuen Daten worldcities_sorted.csv ab.
# Schreibe dazu die Funktion load_cities, sort_cities_by_ascii_name und
# save_cities_to_file.

# 1.b) Länder-Filter
# Erweitere die Aufgabe um einen Länder-Filter: es sollen nur Einträge
# in die neue Datei kommen, die einem eingegebenen Land entsprechen (zb. India)

# Hinweis: 's-Hertogenbosch ist ein güliger Stadtname

import csv
from pathlib import Path


def load_cities():
    """Load Cities from CSV File and return list."""
    ...


def sort_cities_by_ascii_name():
    """Sort cities by column ascii_name and return list."""
    ...


def save_cities_to_file():
    """Save rows to file."""
    ...


def main():
    load_cities()
    ...
