"""
Entpacken von Sequenzen

"""

values = (1, 2, 3)

# klassisch
x = values[0]
x = values[1]
x = values[2]

# pythonisch
x, y, z = values
print(x, y, z)

# unbestimmte Anzahl an Elementen
numbers = [1, 2, 3, 4, 5]
a, *b = numbers
print(f"{a=} {b=}") # in b haben wir eine Liste mit den restlichen Werten

*a, b = numbers
print(f"{a=} {b=}") # in a haben wir eine Liste mit den restlichen Werten

# a und c nehmen den ersten und letzten Wert einer Sequenz. *b nimmt den Rest
a, *b, c = numbers
print(a, b, c)

print("*" * 30)
# Praktische Anwendung

user_input = "3 + 1".split()
print(user_input)
# klassisch über Index-Operator
a = user_input[0]
operator = user_input[1]
b = user_input[2]
print("classic:", a, operator, b)

# pythonische über Entpacken
a, operator, b = user_input
print("pythonic:", a, operator, b)

print(3 + 5)

