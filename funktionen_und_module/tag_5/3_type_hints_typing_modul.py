"""
Das Modul Typing

"""

from typing import Callable, Iterable




def summe(a, b):
    return a + b

def calculator(fn: Callable, a: int, b: int):
    fn(a, b)


calculator(summe, 3, 6)


def print_values(names: Iterable[str]):
    for name in names:
        print(name)

print_values(("tom", "anna"))