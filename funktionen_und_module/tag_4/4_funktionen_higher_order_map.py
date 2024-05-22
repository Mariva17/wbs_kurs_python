"""
Funktionen höherer Ordnung

map(func, seq)
"""
# Map: Elemente einer Sequenz auf eine Funktion abbilden

## 1) Beispiel: Elemente einer Liste quadrieren
values = [1, 2, 3, 4]

values_new = []
for value in values:
    values_new.append(value**2)

print(values_new)

## 2) via List Comprehension
values_new = [value**2 for value in values]
print(values_new)

## 3) via map
values_new = list(map(lambda x: x**2, values))
print(values_new)


list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = [9, 10, 11, 12]

def multiply(a, b, c):
    return a * b * c

result = list(map(multiply, list_a, list_b, list_c))
print(result)

# via List Comprehension
result = [a * b * c for a, b, c in zip(list_a, list_b, list_c)]
print(result)


# Aufgabe: gegeben: liste von strings in int umformen.
# Nutze dazu einmal map und einmal List-Comprehension
string_list = ["1", "4", "n"]

list_int_map = map(int, string_list)
print(list(list_int_map)) # erzeugt ein map-Objekt. Und das muss konsumiert werden.

list_int = [int(el) for el in string_list]
print(list_int)