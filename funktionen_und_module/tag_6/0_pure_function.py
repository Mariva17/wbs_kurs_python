"""
Pure Functions:

- bei gleichem Input immer der gleiche Output
- keine Seiteneffekte

"""

THRESHOLD = 10


def summe(a, b):
    return a + b

result = summe(1, 2)

c = 10

def impure_summe(a, b):
    return a + b + c


result = summe(1, 2)


def filter_values(values):
    # THRESHOLD ist im globalen Scope definiert
    return[value for value in values if value > THRESHOLD]


def filter_values_better(values, threshold):
    # besser: threshold bei call übergeben
    return[value for value in values if value > threshold]

filter_values_better([1, 2], THRESHOLD)





