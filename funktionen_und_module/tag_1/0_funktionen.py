"""
Funktionen: Einführung

"""

# x  = [23, 1]
# y = sorted(x) # Rückgabewert (return) die sortierte Liste

# print_return = print(y) # Rückgabe ist None
# print(print_return)


def hello_world(word):
    # Unterprogramm hello_world
    print(f"Hello new World!: {word}")


hello_world("again")
hello_world("nochmal")
hello_world("zweimal")


# Mini Aufgabe: Schreibe eine Funktion say_hello.
# zwei Parameter: Vorname, Nachname. 
# Soll folgende Aussgabe erzeugen: Trudy Smith says hello.
# Aufruf: say_hello("Trudy", "Smith")
def say_hello(vorname, nachname):
    print(f"{vorname} {nachname} says hello")


say_hello("Trudy", "Smith")