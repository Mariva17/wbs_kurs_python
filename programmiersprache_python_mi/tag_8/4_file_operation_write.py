"""
Öffnen und Schreiben von Dateien (Modus w)
Benötigt keine existierende Datei, wird angelegt oder überschrieben
"""



from pathlib import Path

BASE_DIR = Path(__file__).parent / "data"

# modus w überschriebt den Inhalt
with open(BASE_DIR / "test.txt", mode="w") as f:
    f.write("Das ist eine neue Zeile1\n")
    f.write("Das ist eine neue Zeile2\n")

# Writelines (Schreibt mehrere Elemente einer Liste (ohne newline))
names = ["Bob", "Alice", "Trudy"]
with open(BASE_DIR / "names.txt", mode="w", encoding="utf-8") as f:
    f.writelines(name + "\n" for name in names)