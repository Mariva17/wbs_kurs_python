"""
Öffnen und Einlesen von Dateien (Modus r)

"""

from pathlib import Path

BASE_DIR = Path(__file__).parent / "data"

print("Aktuelles  Arbeitsverzeichnis: ", Path.cwd())
print("ort: ", __file__) # ABSOLUTE Pfad zu der Python-Datei
print("Verzeichnis der Data: ", Path(__file__).parent) # Verzeichnis, in dem die Datei liegt


print("Data: ", Path(__file__).parent / "data")

f = open(BASE_DIR / "test.txt", mode="r", encoding="utf-8") # öffnen
print(f)

content = f.read()
print("a: ", content)

# f.seek(0) # Zurücksetzen des Dateizeigers auf Byte 0
# content = f.read()
# print("b: ", content)

f.close() # IMMER schließen

print("*" * 30)

# der Kontext-Manager with: er schließt Datei nach Verlassen
# des Blocks auch wieder
with open(BASE_DIR / "test.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
# print(f.read()) # f steht nur im Kontext-Manager with zur Verfügung
print("a: ", content)

print("*" * 30)


with open(BASE_DIR / "test.txt", mode="r", encoding="utf-8") as f:
    content = f.readline()
    print(content)
    # content = f.read()
    # print(content)

print("*" * 30)

# Über Datezeiger iterieren und Zeilenweise einlesen (bis zu Newline)
# auch für grosse Dateien geeignet
with open(BASE_DIR / "test.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())