"""
While loop: läuft solange, wie Bedinung wahr ist
"""

# Endlos-Loop: Bedinung bleibt immer wahr
# while True:
#     print("*")


x = 0
y = 10
while x < y:
    x += 1
    print(x)

# Else-Zweig: wird immer ausgeführt, wenn nicht mit break abgebrochen wurde
x = 0
y = 10
while x < y:
    x += 1
    print(x)
else:
    print("Loop beendet!")