"""
Listen kopieren
"""
import sys

fruits = ["apple", "cherry", "banana"]

# unveränderlichen Wert kopieren (hier Integer)
x = 1
y = x # y = 1
x = 3
print(y)

# veränderlichen Wert kopieren (hier Liste)
fruits_neu = fruits # hier wurde nur die Referenz auf die Liste kopiert
print(fruits)
print(fruits_neu)

print("*" * 30)
fruits_neu.append("orange")
fruits.append("melon")
fruits.remove("apple")
print(fruits)
print(fruits_neu)

print(id(fruits), id(fruits_neu))
print("is fruits fruits_neu:", fruits is fruits_neu)

# Liste kopieren
fruits_copy = fruits[:] # flache Kopie (shallow copy)
print(id(fruits_copy))

fruits.append("lemon")

print(fruits)
print(fruits_neu)
print(fruits_copy)

# praktisch kein Nutzen, nur zu Anschauungszwecken
print("ref count von fruits: ", sys.getrefcount(fruits) - 1)


# Verschachtelte Listen kopieren
m = [1, 2, 3, 4, [42]]
m_copy = m[:]
m[0] = 99
m[4].append(11)
print(id(m))
print(id(m_copy))

print(m)
print(m_copy)

