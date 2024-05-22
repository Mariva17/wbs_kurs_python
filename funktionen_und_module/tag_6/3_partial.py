"""
Partial function

"""
from functools import partial

# Aufruf der Funktion park_ticket immer mit allen Argumenten

def park_ticket(region_fix: float, vat: float, price: float) -> float:
    return (region_fix + price) * vat


print(f"Ticket 1: ", park_ticket(region_fix=10, vat=1.19, price=11.2))
print(f"Ticket 2: ", park_ticket(region_fix=10, vat=1.19, price=4))

# Aufruf der Funktion park_ticket immer mit zwei Argumenten


def park_ticket_closure(region_fix: float, vat: float):
    # Problem als Closure lösen
    def inner(price: float):
        return (region_fix + price) * vat
    
    return inner


ticket_calculator_region10 = park_ticket_closure(region_fix=10, vat=1.19)
print(f"Ticket 3: ", ticket_calculator_region10(price=11.8))


# partial aus den functools nutzen. Partial belegt einen Funktionausruf mit Argumenten
# vor und erzeugt einen Funktionsreferenz. Diese Funktionsreferenz kann dann mit
# den verbleibenden Argumenten aufgerufen werden.

park_ticket_pythonic = partial(park_ticket, 10, 1.19)
print(f"Ticket 4: ", park_ticket_pythonic(price=4))