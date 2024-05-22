"""
Ternärer Operator



Python
---------
if a < b:
    x = 10
    else:
        x = 11

x = 10 if a < b else 11

"""
# Erstellen einer sog. boolschen Listen mithilfe des ternären Operators
b = [True if a % 2 == 0 else False for a in range(0, 100) if a > 90]
print(b)
# print(a) # a steht hier nicht mehr zur Verfügung

# kartesisches Produkt
c = []
for a in [1, 2]:
    for b in [3, 4]:
        c.append((a, b))
print(c)

# pythonic
c = [(a, b) for a in [1, 2] for b in [3, 4]]
print(c)

# Dict comprehension
d = [(index, a) for index, a in enumerate("abc")] # list comprehension
print(d)
d = {index: a for index, a in enumerate("abc")} # dict comprehension
print(d)

