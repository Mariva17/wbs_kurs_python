"""
Datei öffnen

"""

from pathlib import Path

filename = "test.txt"
try:
    with open(Path(__file__).parent / filename, mode="r") as f:
        try:
            f.write("some line") # man darf im modus r nicht schreiben
        finally:
            f.close()
            print("finally von innen")

except FileNotFoundError as e:
    print(e, type(e))
    print("Die Datei wurde nicht gefunden")
except OSError as e:
    print("Anderer Fehler: ", e, type(e))
finally:
    print("finally von aussen")
    