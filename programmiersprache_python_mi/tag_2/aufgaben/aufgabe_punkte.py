"""(SCHWER)
Berechne die Distanz zweier Punkte p1(x1, y1) p2(x2, y2)
die Koordinaten sollen über Userinput eingegeben werden
nutze dazu zum Beispiel das math-Modul (zb. für die Squareroot-Methode)
runde das Ergebnis auf 3 Nachkommastellen

prüfung
p1(3, 4)
p2(2, 3)
Distanz: 1.414

"""

import math

print("Hallo User! Willkommen!")
x1 = input("Bitte gebe eine Zahl für Koordinaten eines Punktes: ")
y1 = input("Bitte gebe eine Zahl für Koordinaten eines Punktes: ")
x2 = input("Bitte gebe eine Zahl für Koordinaten anderes Punktes: ")
y2 = input("Bitte gebe eine Zahl für Koordinaten anderes Punktes: ")
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
value = (x2 - x1) ** 2 + ((y2 - y1) ** 2)
distanz = math.sqrt(value)

print("Distanz ist: ", round(distanz, 3))
