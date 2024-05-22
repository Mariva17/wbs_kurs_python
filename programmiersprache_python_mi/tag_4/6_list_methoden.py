"""
List Methoden

"""

fruits = ["apple", "cherry", "banana"] 
name = ["Bob", "Alice", "Trudy"]
print(type(fruits)) # <class 'list'>
print(fruits)
print(f"{id(fruits)=}")

# Länger der Liste
print(f"{len(fruits)=}")

# Auf index 1 zugreifen
print(f"{fruits[1]=}") # "cherry"

# Letzte Elemente eine Liste
print(f"{fruits[-1]=}") # "banana"

# Element an Liste an hängen. append hat (wie viele andere List-Methoden)
# keinen Rückgabewert
fruits.append("melon")
print(fruits)
print(f"{id(fruits)=}")

# Einfügen eines Objekts
fruits.insert(0, "Orange")
print(fruits)

# Löschen eines Objekt
fruits.remove("cherry")
print(fruits)

# pop. Entfernt das letzte Element aus einer Liste, und gibt es zurück
element = fruits.pop()
print(fruits)
print(element)

# pop. Entfernt das letzte Element an Index, und gibt es zurück
element = fruits.pop(0)
print(fruits)
print(element)

# zwei Listen verbinden mit extend
fruits2 = ["coconut", "strawberry"]
fruits.extend(fruits2)
print(fruits)
print(f"{id(fruits)=}")

# oder mit Additions-Operators
fruits = fruits2 + fruits
print(fruits)
print(f"{id(fruits)=}")

# In Operator

if "coco" in "coconut":
    print("coco ist in coconut enthalten")

# Prüfen, ob Element in Liste mit IN-Operator
if "coconut" in fruits:
    print("coconut ist in fruits enthalten")

print("Strawberry steht an Stelle:", fruits.index("strawberry"))

# Ein Element an Index löschen
del fruits[0]
print(fruits)

# Sortieren (lexikographisch)
fruits.sort()
print(fruits)

# An Index 0 ein neues Element einfügen
fruits[0] = "Birne"
print(fruits)

# 3 x 3 Matrix
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Element an Row 1, Column 2
print(m[1][2]) # 6

# umdrehen einer Liste
fruits.reverse()
print(f"{id(fruits)=}")
print(fruits)

fruits = fruits[::-1]  # Erzeugt neue Liste
print(fruits)
print(f"{id(fruits)=}")  # andere ID




