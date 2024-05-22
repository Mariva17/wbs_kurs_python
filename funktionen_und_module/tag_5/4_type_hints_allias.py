"""
Allias, Final, Literal.

Pydentic prüft diese Typenhints für die Datenvalidierung
"""
from typing import Final, Literal


SOURCE_VALUE: Final = 3
WEEKENDS: Final[tuple[str, str]] = ("SAT", "SUN")
Mode = Literal["on", "off"]

matrix = list[list[int]] # Allias


def switch_button(state: Mode):
    print(state)


def fn(m: matrix):
    print(m)


m = [
    [3, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

fn(m)
switch_button("on")   # muss on oder off sein!