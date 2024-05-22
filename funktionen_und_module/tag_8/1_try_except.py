"""
Ausnahmebehandlung

3 Arten von Fehlertypen:
- logische Fehler(Endlos-Loop)
- Syntax Fehler (kann man nichts machen)
- Laufzeitfehler (Runtime Errors) => diese können wir "abfangen

"""

# Prüfen mit Look before you leap
d = {"cat": "Katze"}


if "dog" in d:
    print(d["dog"])
else:
    print("diese key ist nicht vorhanden")

# EAFP (pythonischer Weg)
try:
    print(d["dog"])
except:
    print("diese key ist nicht vorhanden")

print("hier gehts weiter")