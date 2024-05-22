"""
Mengenoperationen, zb. Schnittmenge
"""

x = {"a", "b", "c", "d"}
y = {"a", "b"}

# Schnittmenge
# elemente, die in beiden Menge vorhanden sind

intersection = x & y # Operator
intersection = x.intersection(y) # intersection Methode
print(f"Schnittmenge: {intersection}")

# Differenzemenge
difference = x - y # Operator
difference = x.difference(y)
print(f"Difference: {difference}")

# Union
# Vereinigungsmenge
union = x | y # Operator
union = x.union(y)
print("union:", union)

# ist x eine Obermenge von y?
print("x ist echte Obermenge von y:", x > y)
print("x ist Obermenge von y:", x >= y)
print("x ist Obermenge von y:", x.issuperset(y))

# ist x eine Untermenge von y?
print("x ist echte Untermenge von y:", x < y)
print("x ist Untermenge von y:", x <= y)
print("x ist Untermenge von y:", x.issubset(y))

# Prüfen, ob Liste
names = ["Bob", "Trudy"]
students = ["Bob", "Trudy", "Anna"]
if set(names) <= set(students):
    print("names kleinere als students")