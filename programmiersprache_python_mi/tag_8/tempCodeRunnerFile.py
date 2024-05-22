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