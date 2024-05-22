"""
For_ else - Konstrukt

"""

rabbits = [
    "fiver34",
    "hazel29",
    "bigwig89",
    "blackberry32",
    "buckthorn23",
    "dandelion21",
    "pipkin99",
    "silver22",
    "corn23",
    "hawkbit02",
    "speedwell99",
    "strawberry21",
]

# Aufgabe: Suche nach einem Begriff und falls nicht gefunden, gebe Meldung aus.

# klassischer Ansatz
found = False 

for rabbit in rabbits:
    if rabbit[:-2] == "Fiver":
        print("Rabbit fiver wurde gefunden.")
        found = True
        break
if not found: 
    print("Rabbit wurde nicht gefunden.")

print("*" * 30)
# pythonic for-else
for rabbit in rabbits:
    if rabbit[:-2] == "Fiver":
        print("Rabbit fiver wurde gefunden.")
        break
else:
    # wird immer ausgeführt, wenn NICHT mit breake abgebrochen wurde!
    print("Rabbit wurde nicht gefunden.")

