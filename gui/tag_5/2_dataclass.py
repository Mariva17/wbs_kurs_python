"""
Datenklassen
"""

from dataclasses import dataclass


@dataclass
class Person:
    """Das ist die Datenklasse Person."""

    name: str
    age: int

donald = Person(name="Donald Duck", age=87)
daisy = Person(name="Donald Duck", age=87)
daisy.age = 24  # ändern von Attributen möglich
print(donald)  # Person(name='Donald Duck', age=87)
print(donald == daisy)  # Datenklassen implementieren == (auf allen Attributen)



#  Aufgabe:
# Datenklasse anlegen mit den Attributen rank und suit
# Beschreibt eine Spielkarte.
# für alle Ranks/ Suits sollen Karten angelegt werden => d.h. es soll ein Kartendeck
# angelegt werden (einfach als Liste). Dazu kartesisches Produkt von Ranks und Suits.


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


@dataclass
class Card:
    rank: str
    suit: str


french_deck = [Card(rank=r, suit=s) for s in SUITS for r in RANKS]
print(french_deck[:15])