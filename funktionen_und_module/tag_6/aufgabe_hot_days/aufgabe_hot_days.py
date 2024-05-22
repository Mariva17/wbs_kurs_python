"""
HOT DAYS

Schreibe eine Funktion get_hot_work_days(), die aus der Input-Liste weekday_temperatures  eine neue Liste erstellt und diese zurückgibt.
Diese neue Liste soll nur Tage enthalten, die nicht am Wochenende sind und Temperaturen größer gleich 30 Grad Celcius hatten.
Die Einträge in der neuen Liste sollen als Tupel dargestellt werden (Datum, Temperatur)

Ergebnis:
[('2019-07-15', 31), ('2019-07-16', 33), ('2019-07-19', 30), ('2019-07-23', 31)]

Hinweise: diese Aufgabe optional mit list comprehension oder funktional (map,
filter) lösen.
Nutze Typehints!
"""

from typing import Final


THRESHOLD = 30
WEEKENDS: Final[tuple[str, str]] = ("Saturday", "Sunday")

weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]


def sort_temp(weekdays: list[dict[str, str|int]]):
    res = list(filter(lambda x: x["day"] not in WEEKENDS and int(x["temperature"]) >= THRESHOLD, weekdays))
    result = list(map(lambda x: (x["date"], x["temperature"]), res))
    return result

result = sort_temp(weekday_temperatures)
get_hot_work_days = sorted(result, key=lambda c: c[0])
print(get_hot_work_days)

print("*"*40)
print("Andere Variante")

def create_tuple(d: dict) -> tuple:
    return (d["date"], d["temperature"])

def is_work_day(d: dict) -> bool:
    return d["temperature"] >= THRESHOLD and d["day"] not in WEEKENDS


def get_hot_work_days_list_compr(list: list[dict]) -> list[tuple]:
    return[create_tuple(d) for d in list if is_work_day(d)]

def get_hot_work_days_filter_map(my_list: list[dict]) -> list[tuple]:
    filtered = filter(is_work_day, my_list)
    return list(map(create_tuple, filtered))

def main():
    print(get_hot_work_days_list_compr(weekday_temperatures))
    print(get_hot_work_days_filter_map(weekday_temperatures))


main()