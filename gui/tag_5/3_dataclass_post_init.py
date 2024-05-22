"""
Validierung von Initial-Werten mit __post_init__
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Alter muss positiv sein")


p = Person(name="Tom", age=14)
# p2 = Person("Alice", -5)