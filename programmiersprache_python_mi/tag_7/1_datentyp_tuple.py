"""
Datentyp Tuple: Unveränderlicher, sequentiel

"""

x = 1, 2 # Tuple mit zwei Elementen
y = (1, 3) # Tuple mit zwei Elementen (Klammer ist optional)
z = ()
print(type(z)) # <class 'tuple'>

# Umformet einer Liste in ein Tuple
x = [1, 2, 3]
x_tuple = tuple(x)
print(x_tuple, type(x_tuple))

# Methoden eines Tuple
# count() => Vorkommen zählen
# index() => Index von Element zurückgeben

x = (1, 2, 3, 4)
y = (12, 11, 25, 41)

for i, j in zip(x, y):
    print(i, j)

# per Index zugreifen
print("Element an Index 2:", x[2])
print("Tuple Slicing:", x[0:2], type(x[0:2]))

# 2 Variablen vertauschen
a = 1
b = 2
# Ergebnis soll sein a = 2, b = 1
temp = a
a = b
b = temp
print(f"nach Vertauschen: {a=} {b=}")
# Ergebnis ist a = 2, b = 1

# pytonisch (auf der rechten Seite einen Tupel anlegen und dann entpacken)
a, b = b, a
print(f"nach Vertauschen: {a=} {b=}")


