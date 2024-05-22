"""
Iterator-Funktionen

"""


from typing import Generator
import itertools as it


def infinite_counter():
    x = 0
    while True:
        yield x # Ernte
        x += 1


counter_iterator = infinite_counter()
print("n: ", next(counter_iterator))
print("n: ", next(counter_iterator))
print("n: ", next(counter_iterator))
print("n: ", next(counter_iterator))
print("n: ", next(counter_iterator))


def filter_values_old(values: list) -> list:
    filtered_values = []
    for value in values:
        if value > 10:
            filtered_values.append(value)
    return filtered_values


def filter_values(values: list) -> Generator:
    for value in values:
        if value > 10:
           yield value


#print(list(filter_values([34, 24, 1, 28])))

values = [34, 24, 1, 28, 66, 78, 29]
# filter_obj = filter(lambda x: x > 2, filter_values(values))
# print(list(filter_obj))
# print(next(filter_obj))
# print(next(filter_obj))
filter_obj = filter(lambda x: x > 2, filter_values(values))
print(list(it.islice(filter_obj, 1 , 4))) # Slicing eines Iterators mit islice
