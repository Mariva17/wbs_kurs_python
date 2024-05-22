"""
Structural Pattern Matching (seit Python 3.10)

Schema:
match expression:
    case pattern1: do something
    case pattern2: do something else
    case pattern3: do something more

"""

weekday = 1
weekday_name = ""

if weekday == 1:
    weekday_name = "Monday"
elif weekday == 2:
    weekday_name = "Tuesday"
else:
    weekday_name = "undefined"

weekday = 4

match weekday:
    case 1:
        weekday_name = "Monday"
    case 2:
        weekday_name = "Tuesday"
    case _:
        weekday_name = "undefined"

print(weekday_name)

print("*"*40)

name = "Captain Jean Luc"
#name = "Mr. Bob Black"
match name.split():
    case ["Captaini", *args] as arg:
        print("Captain:", arg, args)
    case ["Captaini", "Jean", "Luc"] as arg:
        print("gesamte Liste:" , arg)
    case first_name, last_name, third_name:
        print(f"Entpacken: {first_name}, {last_name}, {third_name}")
    case _:
        print("Pattern konnte nicht aufgelöst werden")

print("*"*40)

# mit DICT

orders = [
    {"type": "book", "title": "Animal Farm", "author": "G. Orwell"},
    {"type": "book", "title": "1984", "author": "G. Orwell"},
    {"type": "cd", "title": "Dark Side of the Moon", "interpret": "Pink Floyd"},
]

for order in orders:
    match order:
        case {"type": "book", "title": title, "author": author}:
            print("Book order:", order)
        case {"type": "cd", "title": title, "interpret": interpret}:
            print("CD order:", interpret)

print("*"*40)

command = "pick up candle"
command = "pick shovel"
#command = "go north"
weapons = ["sword", "knife"]

match command.split():
    case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"] :
        print("user is picking up:", obj)
    case ["get", obj] | ["pick", "up", obj] if obj in weapons:
        print("user is using weapon:", obj)
    case ["pick", _]:
        print("dieser Gegenstand ist unbekannt")
    case _:
        print("unknown command")

print("*"*40)

# Auf Datentypen prüfen:
val = 33
match val:
    case str():
        print("Val ist vom Typ String")
    case int() | float():
        print("Vai ist vom Typ int oder float")

