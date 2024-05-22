"""(leicht)

1. Gegeben sind zwei Strings. Verkette sie zu einem: Bananarama
a = "A", b = "C"
a = "Banana", b = "rama"
"""
a = "Banana"
b = "rama"
print(a+b)

"""
2. Gegeben sind zwei Strings. Prüfe, ob b in a vorkommt
a = "Bellavista"
b = "vis"

a = "Rom"
b = "Rome"
"""
a = "Bellavista"
b = "vis"
if b in a:
    print("vis ist in", a, "enthalten")
else:
    print("vis ist nicht in", a, "enthalten")

a = "Rom"
b = "Rome"
if b in a:
    print("Rome ist in", a, "enthalten")
else:
    print("Rome ist nicht in", a, "enthalten")

"""
3. String Ersetzung
Ersetze alle Vorkommen von b in a durch c
a = "Bellavista"
b = "Bella"
c = "Buena"

a = "Nordpol"
b = "pol"
c = "kap"
"""
a = "Bellavista"
b = "Bella"
c = "Buena"
a = a.replace(b, c)
print(a)

a = "Nordpol"
b = "pol"
c = "kap"
a = a.replace(b, c)
print(a)