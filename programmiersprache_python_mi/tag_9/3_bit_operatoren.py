"""
Bit Operatoren
10011010101
"""

zahl = 22
print(f"{zahl:08b}")

"""
Dezimalsystem (Basis 10)

Taus    Hund    Zehner   Einser
10^3   10^2     10^1      10^0  (1)

Zahl 825
0        8        2       5

------------------------------------

Binärsystem (Basis 2)

2^7    2^6   2^5   2^4  2^3   2^2   2^1  2^0
128    64     32    16   8     4     2    1

0       0      0     1    0    1     1    0

"""

x = 2
print("Bit left shift: ", x << 1)  # 4 verdoppelt den Wert
print("Bit left shift: ", x << 2)  # 8

x = 23
print(bin(23))  # 64
print(x << 1)

x = 4
print("Bit right shift um eine Stelle:", x >> 2) # teilt den Wert durch 2


print("-" * 30)

# BITWEISE AND (&)
a = 120
b = 78
print(f"{a:08b}")
print(f"{b:08b}")
print(f"{a&b:08b}")

# 01111000
# 01001110  &
# 01001000

# Prüfen, ob eine Zahl gerade ist oder nicht
print(4 & 1) # 0
# 100
# 001  &

print("-" * 30)

#
print("Zweierpotenz Trick")
n = 24
result = (n &(n - 1)) and n != 0
print(f"{n:08b}")
print(f"{(n - 1):08b}")
print(f"{n & (n - 1):08b}")
print("Result von Zweierpotenz Trick:", result)

print("-" * 30)
#------------------------------
# BITWEISE OR
#------------------------------
a = 120
b = 78
print(f"{a:08b}")
print(f"{b:08b}")
print(f"{a|b:08b}")

print("-" * 30)
#------------------------------
# BITWEISE XOR
#------------------------------
a = 120
b = 78
print(f"{a:08b}")
print(f"{b:08b}")
print(f"{a^b:08b}")

x = 1
while x < 4:
    print('*')
    x = x << 1

