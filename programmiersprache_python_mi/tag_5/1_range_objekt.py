"""
Range-Objekt

"""
seq = ["a3", "b4", "c5"]

for i in range(0, 101, 10):
    print(i)

print("*" * 30)

# rückwärts zählen
for i in range(3, 0, -1):
    print(i)

# RANGE OBJEKT
# r = range(100)
r = range(10, 100, 2) # (Start, End, Step)
print(r, type(r))
# Umwandeln in eine Licte
r_list = list(r)
print(r_list)

# Best Praktice: keinen Laufindex angeben, falls er nicht benötigt wird
# Bessere Lesbarkeit
for _ in range(3):
    print("Hello World!")