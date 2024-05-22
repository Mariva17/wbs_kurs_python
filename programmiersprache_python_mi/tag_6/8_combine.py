"""
Dict kann nicht addiren. Nur Combine

c = cities + cities_neu  TypeError!

"""

cities = {
    "hamburg": 100,
    "berlin": 200
}

cities_new = {
    "munich": 200,
    "dresden": 300,
    "hamburg": 1100,
    "bonn": 3
}

# neuere Schreibweise
d = cities | cities_new
print(d)

# ältere Schreibweise
d2 = {**cities, **cities_new}
print(d2)