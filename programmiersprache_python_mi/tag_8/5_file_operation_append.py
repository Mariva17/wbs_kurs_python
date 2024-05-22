"""
An Datei anhängen (Modus a)
Wenn Datei nicht existiert, wird neue Datei erstellt

"""


from pathlib import Path

BASE_DIR = Path(__file__).parent / "data"

names = ["Bob", "Alice", "Trudy"]
with open(BASE_DIR / "names.txt", mode="w", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in names)

names = ["Ted", "Ann"]

with open(BASE_DIR / "names2.txt", mode="a", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in names)


