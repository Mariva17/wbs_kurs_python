"""
leicht
random library bietet Funktionen zum Erstellen von Zufallszahlen
# https://docs.python.org/3/library/random.html

zufallszahl zwischen 1 und 8. Dazu nutzen wir randint(1,8)

Aufgabe: in welchen Wertebereich fällt die Zahl. Schreibe dazu die
nötigen Bedingungen und printe das Ergebnis aus.

a) 6-8
b) 3-5
c) 1-2

Beispiel-Lösung: die gewürfelte Zahl 7 ist im Wertebereich a zuhause

"""

import random

random_number = random.randint(1, 8)
print(random_number)
if 6 <= random_number <=8:
    print("die gewürfelte Zahl", random_number, "ist im Wertebereich a zuhause")
elif 3 <= random_number <= 5:
    print("die gewürfelte Zahl", random_number, "ist im Wertebereich b zuhause")
elif 1 <= random_number <= 2:
    print("die gewürfelte Zahl", random_number, "ist im Wertebereich c zuhause")
else:
    print("die gewürfelte Zahl", random_number, "ist nicht im Wertebereich")