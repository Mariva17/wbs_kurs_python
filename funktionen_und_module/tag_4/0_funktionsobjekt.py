"""
Funktionsobjekt: in Python sind Funktionen "First Class Citizens".

"""

def summe(a, b):
    """Das ist der Docstring."""
    print(a, b)

x = 1
y = 2
summe(x, y)
# Das Funktionsobjekt summe
# nennt man auch Funktionsreferenz
print(summe) # <function summe at 0x00000222E57704A0>

# Eigenschaft _doc_ => Docstring
print("docstring von summe: ", summe.__doc__)
print(summe.__code__.co_name)
print(summe.__code__.co_varnames)
print(summe.__code__.co_firstlineno)

better_summe = summe
print(id(better_summe), id(summe))
better_summe(x, y)



# Taschenrechner

def subtraction(a, b):
    print(a, b)


user_input = "+ 3 3".split()
operator, op1, op2 = user_input

# Alte Methode
if operator == "+":
    summe(op1, op2)
elif operator == "-":
    subtraction(op1, op2)

# Operationsdict mit Funktionsreferenzen
user_input = "+ 3 3".split()
operator, op1, op2 = user_input

operations = {
    "+": summe,
    "-": subtraction,
}


if operator in operations:
    fn = operations[operator] # liefert eine Funktionsreferenz
    result = fn(op1, op2)  # ruft Funktion auf
else:
    raise NotImplementedError("Diese Funktion ist nicht implementiert")






