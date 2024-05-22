"""
Schreibe eine Funktion group_people, die
die Personen aus der Liste people zufällig in
gleich große Gruppen der Größe group_size einteilt.
Die letzte Gruppe darf kleiner als group_size sein.

Nutze dazu random.shuffle()
"""

import random


people = [
    "Bob",
    "Klaus",
    "Peter",
    "Claudia",
    "Petra",
    "Otto",
    "Walter",
    "Benjamin",
]

GROUP_SIZE = 3


def group_people(people, group_size):
    
    random.shuffle(people)
    # group = random.choices(people, k=group_size)

    groups = random.sample([people[i:i + group_size] for i in range(0, len(people), group_size)], k=group_size)
    return groups


groups = group_people(people, GROUP_SIZE)
print(groups)
