"""
Exception Hierarchy

wichtig für PCAP: Lookup Error und Arithmetic Error
"""

# z.B. Lookup Error ist dem Index-Error und dem Key-Error übergeordnet

animals = ["bird", "dog"]

try:
    cat = animals[10] # Index Error
except LookupError as e:
    print("Fehler: ", e, type(e)) # list index out of range


def some_function():
    print("macht irgendwas")
    int("aaa")


try:
    some_function()
except ValueError as e:
    print("in some function ist ein type error ausgelöst worden")

