# leicht bis mittel

# 1. Iteration über Liste (leicht)
"""
Iteriere über die Liste und gebe die Elemente aus!
Zusatzaufgabe: gebe zusätzlich den enstprechenden Index aus,
zb. für Banane den Index 0

0 Banane
1 Apfel
2 Kirsche
"""
fruits = ["Banane", "Apfel", "Kirsche"]
for (index, fruit)  in enumerate(fruits):
    print(f"{index} {fruit}")

# 2. Filtern einer Liste 1 (leicht)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_fruits. Die neue Liste darf nur Elemente enthalten, die mit einem großen B anfangen.

Tip: Nutze dazu die string-Methode startswith oder
den Index-Operator [].

Result: filtered_fruits = ["Banane", "Birne"]
"""
fruits = ["Banane", "Apfel", "Kirsche", "Birne"]
filtered_fruits = []
for fruit in fruits:
    if fruit.startswith("B"):
        filtered_fruits.append(fruit)
print(filtered_fruits)        


# 3. Filtern einer Liste 2 (mittel)
"""
Erstelle aus einer gegebenen Liste eine neue Liste filtered_numbers. Die neue Liste darf nur Elemente enthalten, die größer als 5 sind und kleiner als 100. Die filtered_numbers-Liste muss sortiert ausgegeben werden.

result = [23, 42, 99]
"""
numbers = [1, 4, 5, 2, 42, 2, 1, 99, 23, 23]
filtered_numbers = []
for index, num in enumerate(numbers):
    if 5 < num < 100:
        if num not in filtered_numbers:
            filtered_numbers.append(num)
filtered_numbers.sort()
print(filtered_numbers)        


# 5. das letzte Element (mittel)
"""
Gegeben ist eine Liste, die auch leer sein kann. Prüfe, ob sich mindestens ein Element in der Liste befindet und printe das letzte Element in der Liste.

Erinnerung: eine Liste ist True, wenn sie mindestens
ein Element enthält.
"""
symbols = ["B", "C"]
# symbols = []
if symbols:
    print(f"{symbols[-1]=}")
else:
    print("Die Liste ist leer.")

# 6. erlaubte Werte (mittel)
"""
Gegeben sind zwei Listen:
eine Ausgangsliste a und
eine Liste mit erlaubten Werten allowed_values.

Prüfe für jedes Element in a, ob es in der erlaubten Liste enthalten ist, und füge es einer neuen Liste c hinzu, wenn das zutrifft.

tip:
Iteriere über a und prüfe für jedes Element, ob es erlaubt ist.
Nutze dazu den Membership-Operator in.

result = [50, 200, 50]
"""
a = [50, 100, 40, 20, 200, 50, 100, 10]
allowed_values = [50, 200]
c = []
for elem in a:
    if elem in allowed_values:
        c.append(elem) 
print(c)

# 7. Bereiningen der Liste (mittel)
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente von _ (underscore) und speichere sie in einer neuen Liste. Leere Elemente sollen nicht in die neue Liste aufgenommen werden.

result = [xx, alphabeta]

"""

a = ["x_x", "alpha_beta", "_"]
b = []
for elem in a:
    elem_neu = elem.replace("_", "")
    if elem_neu:
        b.append(elem_neu)
print(b)


# 8. Bereiningen der Liste von Steuerzeichen und x (schwer)
"""
Gegeben ist eine Liste a mit String-Elementen. Bereinige diese Elemente von Whitespace und Steuerzeichen. Entferne alle x aus den Strings.

result = ["halt", "and", "catch", "fire"]
"""
a = ["haxlt ", "\nandx", "\tcatch ", " xfire "]
result = []
for elem in a:
    elem_res = "".join(c for c in elem if c.isalpha())
    elem_res = elem_res.replace("x", "")
    result.append(elem_res)
print(result)