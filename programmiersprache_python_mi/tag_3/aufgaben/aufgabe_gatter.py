A = True
B = True

""" (mittel)
Es sollen Logik-Gatter implementiert werden.
nutze dazu die Variablen A und B, wie in Zeile 1-2 definiert.
Verändere die Werte der Variablen A und B, um die verschiedenen
Gatter zu testen.

"""

"""
Beispiel: das UND-Gatter
"""
if A and B:
    print("A and B ist true")
else:
    print("A and B ist falsh")

"""
Implementiere das XOR-Gatter
# XOR Gatter: XOR ist wahr, wenn exklusiv A oder B wahr ist
# NUtze dazu nicht den XOR-Operator!
https://de.wikipedia.org/wiki/Exklusiv-Oder-Gatter

#
A   B   A XOR B
0   0   0
0   1   1
1   0   1
1   1   0

"""
# XOR-Gatter
if (A and not B) or (B and not A):
    print("XOR is true")
else:
    print("XOR is falsh")

# OR Gatter
if (A and B) or (A and not B) or (B and not A):
    print("OR is true")
else:
    print("OR is falsh")


"""
Das NAND-gatter ist wahr (1), wenn mindestens A oder B falsch (0) ist.
Es ist falsch, wenn A und B wahr sind.
https://de.wikipedia.org/wiki/NAND-Gatter

A   B   A NAND B
0   0   1
0   1   1
1   0   1
1   1   0
"""
# NAND-Gatter
if (not A and not B) or (A and not B) or (B and not A):
    print("NAND is true")
else:
    print("NAND is falsh")

"""
Implementiere das NOR-Gatter mit zwei Eingängen
ein NOR-Gatter ist wahr, wenn A und B falsch sind.
es ist falsch, wenn A oder B wahr ist.
https://de.wikipedia.org/wiki/NOR-Gatter

A   B   A NOR B
0   0   1
0   1   0
1   0   0
1   1   0
"""
if not A and not B:
    print("NOR is true")
else:
    print("NOR is falsh")

"""
Implementiere das XNOR-Gatter (exklusive not or) mit zwei Eingängen
ein XNOR-Gatter ist wahr, wenn entweder A und B falsch ODER A und B wahr sind.
https://de.wikipedia.org/wiki/XNOR-Gatter

A   B   A XNOR B
0   0   1
0   1   0
1   0   0
1   1   1
"""
# XNOR-Gatter
if  (not A and not B) or  (A and B):
    print("XNOR is true")
else:
    print("XNOR is falsh")