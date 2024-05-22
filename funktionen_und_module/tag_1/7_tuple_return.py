"""

Mehrere Rückgabewerte einer Funktion via Tuple

"""

def multiplier(value):
    # Rückgabewert: a, b
    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    return square(value), cube(value)


x = multiplier(4)
print(x)

s, c = multiplier(4)
print(s, c)