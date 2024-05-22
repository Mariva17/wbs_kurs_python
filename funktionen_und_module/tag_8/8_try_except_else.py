"""
der Else-Zweig: wird immer ausgeführt, wenn keine Exception ausgelöst wurde (Egal, ob aufgefangen oder nicht)

"""

x = 10
try:
    p = int("u")
    u = x / 2
except ValueError:
    print("hier ist ein Value Error aufgetreten")
else:
    print("else: wird immer aufgerufen, wenn KEINE Exception ausgelöst wurde")
finally:
    print("finally: wird immer ausgeführt")