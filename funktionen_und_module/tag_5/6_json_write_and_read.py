"""

Json-Daten schreiben mit json.dump

"""

import json
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

persons = [
    {"name": "Alice", "age": 41},
    {"name": "Älan", "age": 31},
    {"name": "Trudy", "age": 45},
    {"name": "Bob", "age": 51},
]


with open(BASE_DIR / "data.json", mode="w", encoding="utf-8") as f:
    json.dump(persons, f, indent=4, ensure_ascii=False)

with open(BASE_DIR / "data.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)

print("Wiederhergestellte Daten")
print(data)