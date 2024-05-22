"""
Der Walrus-Operator (Zuweisungsoperator)
Eingeführt in Python 3.8
:=
"""
fruits = ["ab", "cd", "df"]

if len(fruits) > 2:
    print("Die Länge der Fruits-liste ist:", len(fruits))

length_of_fruits = len(fruits)
if length_of_fruits > 2:
    print("Die Länge der Fruits-liste ist:", length_of_fruits)

if (laenge := len(fruits)) > 2:
    print("Die Länge der Fruits-liste ist:", laenge)

print("*" * 40)

while (value := input("Enter a digit:")).isdigit():
    print(value)

print("*" * 40)

