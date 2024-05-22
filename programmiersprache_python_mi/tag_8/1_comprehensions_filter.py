"""
Filter in List Comprehensions einsetzen

"""

seq = [2, 4, 7, 8]

# klassisch
seq_klein = []
for el in seq:
    if el < 4:
        seq_klein.append(el)
print(seq_klein)

# via List comprehension
seq_klein = [el for el in seq if el < 4]
print(seq_klein)

names = ["bob", "alice"]
name_length = [len(name) for name in names]
print(name_length)

names = ["bob", "alice"]
[print(name) for name in names]

# Aufgabe: Alle Personen in neue Liste, die mit großem "B" anfangen UND einem kleinen n enden
personen = ["Bernd", "Klaus", "Peter", "Claudia", "Petra", "Benjamin"]

result = [person for person in personen if person.startswith("B") and person.endswith("n")]
print(result)


