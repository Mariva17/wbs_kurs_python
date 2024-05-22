"""
String formatieren

"""

x = 34
y = 58

print("x=", x)
print(f"{x=}, {y=}")

# Zahlensystem
print(f"dec: {x:#d}, hex: {x:#x}, oct: {x:#o}, bin: {x:#b}")

# float formatiwren
x = 5.46513213
print(f"{x: .2f} {1/3: .2f}") # auf zwei Nachkommastellen runden
print("{: .2f}".format(x))

# Prozentuales Verhältnis
points = 19
total = 22
print("Richtige Antworten: {:.2f}". format(points / total)) # 0.86
print("Richtige Antworten: {:.2%}". format(points / total)) # 86.36%


big_number = 1000000000
print(f"{big_number:_}") # 1_000_000_000
print(f"{big_number:,}") # 1,000,000,000