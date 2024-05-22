"""
Reduziert ein Iterable auf einen Wert

schema: reduce(func, iterable, [startwert])

"""
import operator as op
from functools import reduce

values = [1, 2, 3, 4, 5]

produkt = reduce(op.mul, values)
print(produkt)

produkt = reduce(op.mul, values, 100)
print("Mit startwert: ", produkt)


