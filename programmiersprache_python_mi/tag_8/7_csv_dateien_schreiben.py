"""
CSV Dateien schreiben

"""
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent / "data"

data_rows = [
    [34, 2, 42, 54],
    [25, 8666, 954, 4556],
    [234, 247, 355, 6544]
]

with open(BASE_DIR / "data_new.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["id", "x", "y", "z"]) # Eine Headerzeile schreiben
    writer.writerows(data_rows) # Daten schreiben

## DICT writer
data_dict = [
    {"id": 3, "name": "Alice"},
    {"id": 4, "name": "Alan"}
]

with open(BASE_DIR / "data_names.csv", mode="w", newline="") as f:
    fieldnames = ["id", "name"]
    writer = csv.DictWriter(f, fieldnames= fieldnames, delimiter=",")
    writer.writeheader()
    writer.writerows(data_dict)