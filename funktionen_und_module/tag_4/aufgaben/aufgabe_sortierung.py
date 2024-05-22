
import string

# 1. Sortiere nach Einwohner (LEICHT)
lst = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]

lst_einwohner = sorted(lst, key=lambda x: x[0])
print("Aufgabe 1: Einwohner - ", lst_einwohner)
print("*" * 40)

# 2. Sortiere nach Bundesstaaten (Alabama, California...) LEICHT
states = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
]

lst_states = sorted(states, key=lambda x: x[1])
print("Aufgabe 2: Nach States - ", lst_states) 
print("*" * 40)

# 3. Sortiere absteigend (LEICHT)
lst = [500, 1000, 400, 40000, 999, 2, 0.5, 17]
lst_sorted = sorted(lst, reverse=True)
print("Aufgabe 3: ", lst_sorted)
print("*" * 40)


# 4a) Sortiere nach Vornamen(MITTEL)
# 4b) Sortiere nach id (entferne alle Nicht-Zahlen, zb. 42ai => 42)
people = [
    {
        "first": "Arthur",
        "last": "Dent",
        "id": "123s",
    },
    {
        "first": "Zaphod",
        "last": "Beeblebrox",
        "id": "42ai",
    },
    {
        "first": "Ford",
        "last": "Perfect",
        "id": "233",
    },
]

lst_people_vorname = sorted(people, key=lambda x: x["first"])
lst_people_vorname2 = sorted(people, key=lambda x: x.get("first", ""))
print("Aufgabe 4a: People nach Vornamen - ", lst_people_vorname) 
print("Aufgabe 4a: People nach Vornamen - ", lst_people_vorname2) 
print("*" * 40)


def sort_id(value):
    return int("".join(char for char in value if char.isdigit()))

lst_people_id = sorted(people, key=lambda el: sort_id(el["id"]))
#lst_people_id = sorted(people, key=id_num)
print("Aufgabe 4b: People nach id - ", lst_people_id) 
print("*" * 40)



# 5. Sortiere nach Punkten (aufsteigend) LEICHT
player = {"peter": 100, "klaus": 34, "wizz": 222, "angela": 23, "sabine": 400}
print("Aufgabe 5: Nach Punkte - ", sorted(player.items(), key=lambda el: el[1]))
print("*" * 40)

# 6 Gegebene eine Liste mit Personen und deren Verkäufen. MITTEL
# Der Verkaufserlös errechnet sich durch die letzten beiden Positionen,
# z.b. 46 x 18.67 für John Miller. Sortiere nach Verkaufserlös
umsaetze = [
    ("John", "Miller", 46, 18.67),
    ("Randy", "Steiner", 48, 27.99),
    ("Tina", "Baker", 53, 27.23),
    ("Andrea", "Baker", 40, 31.75),
    ("Eve", "Turner", 44, 18.99),
    ("Henry", "James", 50, 23.56),
]
#print(sorted(umsaetze))

def gain(x):
    g = x[2] * x[3]
    return g

lst_gain = sorted(umsaetze, key=gain)
print("Aufgabe 6: Verkaufserlös - ",lst_gain)
print("*" * 40)


# 7. Sortiere aufsteigend nach max-Wert der Liste. SCHWER
stox = [
    ["a", [22, 25, 14, 23]],
    ["b", [122, 25, 14, 233]],
    ["c", [422, 25, 14, 33]],
    ["d", [22, 1025, 14, 33]],
    ["e", [2, 5, 4, 3]],
]
#print(dict(sorted(stox)))
stox = dict(stox)
print(sorted(stox.items()))
def fn_stox(x):
    s = sum(x[1])
    return s
result = sorted(stox.items(), key=fn_stox)
print("Aufgabe 7: Nach max-Wert  - ", list(result))
print("*" * 40)

# 8 Sortiere aufsteigend nach Modul-Name
"""
es soll nur nach dem Modul-Namen sortiert werden, z.b. pytest,
nicht nach der Version oder der Plattform.

falsch: ['pre-commit', 'pytest-cov', 'pytest==5.2', "waldo-parillo;sys_platform=='win32'"]

richtig: ['pre-commit', 'pytest==5.2', 'pytest-cov', "waldo-parillo;sys_platform=='win32'"]
"""

modules = [
    "waldo-parillo;sys_platform=='win32'",
    "pytest==5.2",
    "pytest-cov",
    "pre-commit",
]

print(sorted(modules))

def fn(x):
    
    for i in x:
        if not i.isalnum():
            x = "".join(i)
    return x

result = sorted(modules, key=fn)