"""
Sortieren mit Lambda und key

"""

values = [3, 5, 7, 1, 12]
sorted_values = sorted(values)
print(sorted_values) # [1, 3, 5, 7, 12]


chars = ["a", "f", "c", "e", "d"]
sorted_chars = sorted(chars)
print(sorted_chars) # ['a', 'c', 'd', 'e', 'f']


chars = ["a", "f", "b", "B", "A", "c", "e", "d"]
sorted_chars = sorted(chars)
print(sorted_chars) # ['A', 'B', 'a', 'b', 'c', 'd', 'e', 'f']


# Keyword-Argument key
chars = ["a", "f", "b", "B", "A", "c", "e", "d", "E"]
sorted_chars = sorted(chars, key=lambda el: el.lower()) 
print(sorted_chars) # ['a', 'A', 'b', 'B', 'c', 'd', 'e', 'E', 'f']

print("*"*30)

snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}

snacks_sorted = sorted(snacks)
print(snacks_sorted) # ['Kekse', 'Milka', 'Snickers']

print("*"*30)

snacks_sorted = sorted(snacks.items())
print(snacks_sorted) # [('Kekse', 5.2), ('Milka', 3.3), ('Snickers', 1.5)]

print("*"*30)

snacks_sorted_preis = sorted(snacks.items(), key=lambda el: el[1])
print(snacks_sorted_preis) # [('Snickers', 1.5), ('Milka', 3.3), ('Kekse', 5.2)]

print("*"*30)


# Aufgabe: Sortiere nach id (Numerisch). Also nur nach Index 2
ids = ["id5", "ix1", "id2", "ia5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda el: el[-1])
print(ids_sorted) # ['ix1', 'id2', 'id3', 'id4', 'id5', 'ia5']

# nach zwei Indexen
ids = ["id5", "ix1", "id2", "ia5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda el: el[-2:-1])
print(ids_sorted) # ['ia5', 'id5', 'id2', 'id4', 'id3', 'ix1']

ids = ["id15", "ix11", "ir21", "ia15", "ix4", "id33"]
ids_sorted = sorted(ids, key=lambda el: int(el[2:]))
print(ids_sorted) # ['ix4', 'ix11', 'id15', 'ia15', 'ir21', 'id33']

print("*"*30)

snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}


# Sortieren nach Preis
print(sorted(snacks.items()))
snacks_nach_preis = sorted(snacks.items(), key=lambda el: el[1]["price"])
x = dict(snacks_nach_preis)
print(x)

print("*"*40)

# Sortieren nach Preis und Amount

snacks2 = {
    1: {"name": "Erdnüsse", "price": 100, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 200, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 200, "amount": 10, "pos": {"x": 50}},
}
snacks_nach_preis_am = sorted(snacks2.items(), key=lambda el: (el[1]["price"], el[1]["amount"]))

x = dict(snacks_nach_preis_am)
print("snacks_nach_preis_am: ",  x)

print("*"*40)
# Sortieren nach Stringlänge
monty_crew = ["Cleese", "Idle", "Palin", "Chapman", "Gilliam", "Jones"]
print(sorted(monty_crew, key=lambda x: len(x)))
print(sorted(monty_crew, key=len))


