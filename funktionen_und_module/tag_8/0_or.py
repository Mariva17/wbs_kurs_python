"""
Operator OR
or liefert entweder den linkenoder den rechten operanden
als Rückgabewert
"""


x = ""
y = 12

print(x or y) # shorthand ternary operator

def hello(x):
    print(x)

hello("Alice" or "Bob") # hier wird Alice übergeben
hello("" or 0.0) # wenn beide falsy sind, wird 0.0 übergeben

