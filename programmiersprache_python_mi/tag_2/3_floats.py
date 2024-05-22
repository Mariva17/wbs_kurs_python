"""
Fließkommazahl (float), IEEE 754
Zahlenmenge der reelen  Zahlen R
3.223

Decimal-Package (import decimal)
scipy - Package

"""
import math
import cmath

c = 0.7568
print("Typ c:", type(c)) # Object der Klasse float

x = 4 / 3
print(x)  # ohne Rundung
print(round(x, 2)) # mit Rundung auf zwei Nachkommastellen

#TypeCasting int -> float, float -> int
# Umwandeln von einem float zu einem Int
x = 2.8
x_int = int(x)
print("x int:", x_int)

# Umwandeln von einem Int zu einem float
x_float = float(x_int)
print("x float:", x_float)

# Besondere float-Werte
# infinity (definiert in dem IEEE-Standart 754)
neg_inf = float("-inf")
pos_inf = float("inf")
print(type(pos_inf))

# Nan-Wert
nan = float("nan")
print(type(nan))

# wissenschaftlich Notation
x = 3.45e-4 # * 10 ** -4
print(x)

result = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(result)

# Floor-Funktion (Gauss-Klammer). Erzeugt ein Int
result = math.floor(3.76)  # 3
print(result)
result = math.floor(-4.4)  # -5
print(result)

# Ceil-Funktion (Aufrunden zum nächsthöhren Int)
result = math.ceil(3.76)  # 4
print(result)
result = math.ceil(-4.4)  # -4
print(result)

# Quadratwurzel
print("Quadratwurzel: ", math.sqrt(4))

# Konstanten
PI = math.pi
E = math.e