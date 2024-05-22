"""
Datentyp complex.
Komplexe Zahlen

"""

import cmath


z = complex(3, 2)
print(z, type(z)) # (3+2j) <class 'complex'>
print("Reateil: ", z.real, "Imaginärteil:", z.imag)

# Zahl direkt erstellen
z = 3 + 2j
print(z)


# abs()
z1 = 3 + 4j
print("abs:", abs(z1)) # abs: 5.0 Magnitude


# Polarkoordinatoren
magnitude, angle = cmath.polar(z)
print(magnitude, angle)

z_from_polar = cmath.rect(magnitude, angle)
print(z_from_polar)


