"""
Built-in Funktionen: all und any

hier: all

"""

# all: ergibt True, wenn alle Elemente eines Iterables truthy sind
# d.h. als wahr evaluiert werden können
x = [1, 2, 3]
print(all(x)) # True

y = 11
x = 5
# if x > 3 and y > 8 and x + 4 > 11
if all([x > 3, y > 8, x + 14 > 11]):
    print("all ist wahr")
    print([x > 3, y > 8, x + 14 > 11])



values = [2, 2.2, 4, 2.3, 0.1]
interval = (1, 5.3)

def check_values(val, interval):
    a, b = interval
    result = all(a <= value <= b for value in val) 
    print(result)


result = check_values(values, interval)


x = False, False # Tuple
print(x)
print(all((False, False)))