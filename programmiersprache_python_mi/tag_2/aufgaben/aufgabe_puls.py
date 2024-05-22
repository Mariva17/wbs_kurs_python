"""(leicht)
Aufgabe:
 Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. Er lässt sich
 mit der Formel Puls = 165 - 0.75 * Alter bestimmen.

So ist der optimale Puls für 18 Jahre 152
Schreibe ein Programm, das folgenden Dialog ermöglicht:

Alter: über input einzugeben
Ausgabe: optimaler Puls

Runde das Ergebnis auf 0 Nachkommastellen, damit sich eine ganze Zahl ergibt.
"""

import math

print("Hallo User! Willkommen!")
alter = input("Bitte gebe dein Alter ein: ") 
alter = int(alter)
puls = 165 - (0.75 * alter)
print(math.ceil(puls))