"""
(mittel)

Über eine Usereingabe sind zwei Kreise k1 und k2 einzugeben. Diese Kreise sind
definiert durch Radius und Position im kart. Koordinatensystem.

Eingabe:
Position und Radius der beiden Kreise

Aufgabe:
Schneiden sich die Kreise oder ist ein Kreis in einem anderen enthalten?

Hinweise:
----------
- Die Kreise schneiden sich, wenn der Abstand der Mittelpunkte kleiner ist
  als die Summe der Radien.
- Die Kreise schneiden sich nicht, wenn der Abstand der Mittelpunkte größer
  ist als die Summe der Radien.
- Ein Kreis ist im anderen enthalten, wenn der Abstand der Mittelpunkte kleiner
  ist als der Radius des größeren Kreises minus der Radius des kleineren
  Kreises (nutze hierzu die Funktion abs).
- Die Kreise sind kongruent, wenn der Abstand der Mittelpunkte gleich 0 ist
  und die Radien gleich sind.
- Die Kreise berüren sich, wenn der Abstand der Mittelpunkte gleich der
  Summe oder der Differenz der Radien ist.

Beispiel:
----------
Bitte geben Sie den Radius des ersten Kreises ein: 5
Bitte geben Sie die x-Position des ersten Kreises ein: 0
Bitte geben Sie die y-Position des ersten Kreises ein: 0

Bitte geben Sie den Radius des zweiten Kreises ein: 5
Bitte geben Sie die x-Position des zweiten Kreises ein: 10
Bitte geben Sie die y-Position des zweiten Kreises ein: 20

Die Kreise schneiden sich nicht.

"""
import math

r1 = float(input("Bitte geben Sie den Radius des ersten Kreises ein: "))
x1 = float(input("Bitte geben Sie die x-Position des ersten Kreises ein: "))
y1 = float(input("Bitte geben Sie die y-Position des ersten Kreises ein: "))

r2 = float(input("Bitte geben Sie den Radius des zweiten Kreises ein: "))
x2 = float(input("Bitte geben Sie die x-Position des zweiten Kreises ein: "))
y2 = float(input("Bitte geben Sie die y-Position des zweiten Kreises ein: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(d)

if d < (r1 + r2):
  print("Die Kreise schneiden sich.")
else:
  print("Die Kreise schneiden sich nicht.")

if r1 > r2:
  if d < abs(r1-r2):
    print("Ein Kreis ist im anderen enthalten")
elif r2 > r1:
  if d < abs(r2-r1):
    print("Ein Kreis ist im anderen enthalten")
else:
  print("Ein Kreis ist im anderen nicht enthalten")

if d == 0 and r1 == r2:
  print("Die Kreise sind kongruent.")  
else:
  print("Die Kreise sind nicht kongruent.")

if d == (r1+r2) or d == abs(r1-r2):
  print("Die Kreise berüren sich.")
else:
  print("Die Kreise berüren sich nicht.")