"""
Ganzzahlen

** Exponentation
% Modulo-Operator (Rechnen mit Rest)
"""

# Underscore als Trenner
amount = 100_000_000

# NICHT das Komma, das hier erzeugt ein Tupel!
amount = 100,000,000
print(amount)

# Modulo-Operator (Rechnen mit Rest)
x = 10
y = 3
result = x % y
print("Modulo Ergebnis:", result)

# Prüfen, ob eine Zahl gerade ist.
result_modulo = 5 % 2
result_div = 5 // 2
print(result_modulo)
print(result_div)


"""
Wieviele Baumstämme passen der Länge nach in die Halle.
Baumstamm-Länge 4, Hallenlänge 19. Wieviele Meter sind noch übrig?
Nutze Konstanten und Variablen.
"""
HALLENLÄNGE = 19
baumstamm_länge = 4
total_trees = HALLENLÄNGE // baumstamm_länge
total_rest = HALLENLÄNGE % baumstamm_länge
print("Es passen in die Halle", total_trees, "Baumstämme")
print("Es ist übrig:", total_rest, "Meter")

# Exponentation
# **
x = 4
y = 2
result = x ** y
print("Ergebnis 4**2:", result)

# Vorsicht: Exponentation bindet stärker als unäras Minus (negative)
# https://docs.python.org/3/reference/expressions.html#operator-precedence
result = -4 ** 2 # -16

# Division (True div) erzeugt IMMER ein float
result = 6 / 3
print("Result Division:", result)
