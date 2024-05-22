"""
CSV - Dateien einlesen (CSV sind Datenaustausch Dateien)
"""
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent / "data"

VALUE = 1
SQMT = 2

# eigener Ansatz
with open(BASE_DIR / "daten.csv", mode="r", encoding="utf-8") as f:
    for line in f:
        values = line.split(",")
        print(values, len(values))

print("*" * 40)

# Datei daten.csv einlesen
with open(BASE_DIR / "daten.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    header = next(reader)
    print("header:", header)
    for row in reader:
        print(row, len(row))
        value = (float(row[VALUE]) + float(row[SQMT])) / 2
        print(value)

print("*" * 40)

# Datei user einlesen (Semikolon-Separiert)
with open(BASE_DIR / "user.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)

print("*" * 40)

# DICT-Reader. Liest Zeilen ein und erstellt pro Zeile ein Dict
# aus Header und Werten
with open(BASE_DIR / "user.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        print(row)
        print(row["name"])

print("*" * 40)

# Bei Datei ohne Headerzeile fieldnames mit angeben. Länge muss der Anzhal der Spalten entsprechen
with open(BASE_DIR / "daten_kein_header.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=",", fieldnames=["id", "value", "squaremt", "city"])
    for row in reader:
        print(row)