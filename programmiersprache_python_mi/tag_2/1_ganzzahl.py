"""
Modul-Docstring
Ganzzahlen, Datentyp Integer
Z

arithmetische Operatoren:
+ Additionsoperator
- Subtraktion
/ Divisionsoperator (true div)
// Floor-Division
* Multiplikationsoperator
** Exponentation
% Modulo-Operator (Rechnen mit Rest)



"""

# das ist ein Zeilenkommentar

# Integer kennen keine Grenze
x = -23568971456622478888884713156484761413113184787489797997
print(x)
print(type(x))

# Ganzzahl Addition (+)
distance_1 = 100
distance_2 = 330
distance_total = distance_1 + distance_2

# Division (Divisionsoperator /)
# Ergebnis einer Division ist IMMER ein float
x = 4
y = 2
result = x / y # 4 / 2
print(result)
print(type(result))

# Division durch 0
# result = 4 / 0 (ZeroDivisionError: division by zero)

# Floor-Division, Abrundungs-Division (Divisionsoperator //) Gaußklammer
x = 5
y = 2
result = x // y 
print(result) # 2
print(type(result))

# Multiplikation
x = 15
y = 2
result = x * y
print(result)


# Konvention: Großgeschriebene Variablen sind Konstanten
# und sollten nicht verändert werden.
THRESHOLD = 20

"""
Aufgabe:
Ein Raum fasst maximal 10 Personen. Zur Zeit befinden sich eine
unbekannte Anzahl an Personen in diesem Raum.
Wieviele Personen können den Raum noch betreten?
Lege passende Variablen/Konstanten an und führe die Berechnung durch.

Singular und Plural sowie negative Anzahl an Personen im Ergebnis-Print
sind zu ignorieren.
"""
MAXIMAL_PERSONEN = 10
momentane_personen = 7
momentane_personen = 8
result = MAXIMAL_PERSONEN - momentane_personen
print("In diesem Raum", "passen noch", result, "Personen.")
