"""
Lese die Datei diabetes2.csv mit Hilfe der csv-Library ein.
Auf Basis dieser Datei soll eine neue Datei erstellt werden, die nur
die Spalten BMI, age und outcome berücksichtigt.
Ferner sollen nur Einträge berücksichtigt werden
mit outcome = 1

Schreibe die Daten kommasepariert in eine neue Datei:
diabetes_positive_outcome.csv

Außerdem interessieren uns folgende Werte, die am Ende des Schreibvorgangs
noch ausgegeben werden sollen:

Für alle Einträge mit outcome=1
Mittelwert BMI
Mittelwert Alter
Median BMI
Median Alter
Max BMI, Min BMI
MAX BloodPRESSURE

für Median und Mittelwert nutze das statistics Modul
import statistics
median = statistics.median([2, 3, 4, 5])
mean = statistics.mean([2, 3, 4, 5])

für min/max nutze die Builtin-Funktionen min([1, 2, 3])
und max([3, 2, 1])

"""

from pathlib import Path
import csv
import statistics

BASE_DIR = Path(__file__).parent 

# data_rows = []

# csv Datei einlesen
with open(BASE_DIR / "diabetes2.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=",")
    data_rows = [*reader]
 #   print(data_rows)

# Datentyp korrigieren
for row in data_rows:
    values = list(row.values())
    values[:] = *map(int, values[:5]), *map(float, values[5:7]), *map(int, values[7:])
    row.update(zip(row.keys(), values))

# gefilterte neue Liste
new_data = [[row["BMI"], row["Age"], row["Outcome"]] for row in data_rows if row["Outcome"] == 1]

# als csv schreiben
with open(BASE_DIR / "diabetes_positive_outcome.csv", mode="w", newline="\n") as f:
    writer = csv.writer(f)
    writer.writerow(["BMI", "Age", "Outcome"])
    writer.writerows(new_data)

# gelfilterteListe wird nicht mehr benötigt
del new_data

print("Statistik:")

print("Mittelwert BMI = ", statistics.mean(row["BMI"] for row in data_rows if row["Outcome"] == 1))
print("Mittelwert Alter = ", statistics.mean(row["Age"] for row in data_rows if row["Outcome"] == 1))
print("Median BMI = ", statistics.median(row["BMI"] for row in data_rows if row["Outcome"] == 1))
print("Median Alter = ", statistics.median(row["Age"] for row in data_rows if row["Outcome"] == 1))            
print("Max BMI = ", max(row["BMI"] for row in data_rows if row["Outcome"] == 1))
print("Min BMI = ", min(row["BMI"] for row in data_rows if row["Outcome"] == 1))
print("Max BloodPRESSURE = ", max(row["BloodPressure"] for row in data_rows if row["Outcome"] == 1))
