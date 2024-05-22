"""
einfach

Gib zwei Zahlen a und b aufwärts sortiert aus.
Verwende einfache Datentypen wie int. Keine Listen, sort() oder ähnliches.


Prüfe den Algorithmus mit folgenden Zahlen
a = 9, b = 8
a = 9, b = 10

Beispiel
a = 3
b = 2

Antwort:
2, 3
"""

a = 9
b = 8
if a > b:
    print(b, a, sep=", ")
else:
    print(a, b, sep=", ")

"""
mittel

Bestimme die Größte aus drei vorher festgelegten Zahlen und gib diese Zahl aus.
Verwende einfache Datentypen wie int. Keine Listen, sort() oder ähnliches.

Prüfe mit folgenden Zahlen:
a = 2, b = 343, c = 1
a = 12, b = 3, c = 2
a = 4, b= 11, c = 24

Beispiel
a = 33, b = 12, c = 2
Antwort:
Die größte Zahl ist a mit dem Wert 33
"""
a = 12
b = 3
c = 2
if a >= b and a >= c:
    print("Die größte Zahl ist a mit dem Wert", a)
elif b > a and b >= c:
    print("Die größte Zahl ist b mit dem Wert", b)
elif c > a and c > b:
    print("Die größte Zahl ist c mit dem Wert", c)
else:
    print("die Zahl ist falsh")


x = True
k = x + 3
print(k)