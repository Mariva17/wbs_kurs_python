"""

Iterable vs Iterator

Iterable
------------
etwas, über das iteriert werden kann. Dazu muss die Klasse (zb. list)
die__iter__()-Methode implementieren

Iterator (Objektfabrik, liefert das nächste Objekt)
-----------------------------------------
ein Iterator implementiert die __next__()-Methode. Ruft immer das nächste Objekt auf
"""

print(dir(list)) # implementiert eine __iter__()-Methode

names = ["bob", "anna", "grampy"] # eine Liste ist KEIN Iterator
names_iterator = iter(names) # iter ruft die __iter__()-Methode
print(next(names_iterator))

for el in names_iterator:
    print(el)

# Iteratoren verbrauchen sich. Wenn sie am Ende
# sind, gibt's keine Ausgabe mehr
for el in names_iterator:
    print(el)


print("*" * 40)

# wie funktioniert for loop unter der haube?
names = ["bob", "anna", "Trudy", "Jonny"] 
names_iterator = iter(names)

while True:
    try:
        element = next(names_iterator)
        print(element)
    except StopIteration:
        break

print("*" * 40)

# Über ein set iterieren
numbers = {2, 53, 54, 28}
# number_iterator = iter(numbers) # Set-Iterator
for number in numbers:
    print(number)