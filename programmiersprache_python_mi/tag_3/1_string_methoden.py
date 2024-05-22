"""
Strting - Methoden
"""

# Funktion len um länge eines strings zu ermitteln
name = "Thrudy"
print("Länge von Name: ", len(name))

example = "the quick brown fox"
print(type(example))

# Ersetzen von Vorkommen
example_replaced = example.replace("o", "a")
print(example_replaced)
user_input = "2,343"
number = user_input.replace(",", ".", 1) # 2.343 (erste)
number = float(number)


# COUNT: Zeichen zählen. 1. Argument Suchstring; 2. Argument ist Startwert
example = "the quck brown fox fox"
fox_count = example.count("fox")
print("fox_count: ", fox_count)
fox_count = example.count("fox", 18) # ab 18 Zeichen count
print("fox_count: ", fox_count)

# find und index
#find prüft, an welchem Index ein Suchwort vorkommt (-1 wenn nicht vorhanden)
example_find = example.find("brown")
print("example_find: ", example_find)
example_find = example.find("brow")  # -1 (wenn nicht vorhanden)
print("example_find: ", example_find)
example_find = example.find("brow")   #  (ValueError wenn nicht vorhanden)
print("example_find: ", example_find)


# upper/lower/ casefold
example_upper = example.upper()
print(example_upper)

example_lower = example.lower()
print(example_lower)

city = input("Bitte gebe deine Stadt ein: ")
print("Eingabe: ", city)
print("lower: ", city.lower())
print("capitalize: ", city.capitalize())
print("title: ", city.title())

example = "weiße Wälle"
print(example.lower())
print(example.casefold())

# Bereinigen von Whitespace und Steuerzeichen von vorne und hinten: strip
user_input = "\t 3.34 \r\n"
print(user_input)
user_input_cleaned = user_input.strip()
print(user_input_cleaned)

user_input = "***$%&3.34$%&**"
user_input_cleaned = user_input.strip("*$%&") # vorsicht: newlines und co werden nicht mehr entfernt!
print(user_input_cleaned)

# Bereinigen von Whitespace und Steuerzeichen von hinten (rechts): restrip
user_input = "\t 3.34 \r\n"
user_input_cleaned = user_input.rstrip() # right strip
print("rstripped: ", user_input_cleaned)
user_input_cleaned = user_input.lstrip() # left strip
print("lstripped: ", user_input_cleaned)

