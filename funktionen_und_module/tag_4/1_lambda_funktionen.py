"""
Lambda Funktionen: Anonyme Funktionen

"""

def fn(x):
    return x**2

fn # Funktionsreferenz

f = lambda x: x**2 # Parameter x, Rückgabewert x**2
f # Funktionsreferenz
print("Aufruf von Funktionsreferenz: ", f(3))

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

result = operations.get("+")(1, 2)
print("Result: ", result)


# Sofortiges Aufrufen einer Lambda-Funktion
# Immediately Envoked Function Expression
print((lambda x: x**2)(10)) # 100

