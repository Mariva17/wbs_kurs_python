"""
Über ein Dict iteration

"""


capitals = {
    "Hessen": "Wiesbaden",
    "Saarland": "Saarbrücken",
    "Baden-Württemberg": "Stuttgart",
    "Rheinland-Pfalz": "Mainz",
    "Nordrhein-Westfalen": "Düsseldorf",
}

# Iterieren über die Keys eines Dicts
for key in capitals:
    print(key)
 #   print(capitals[key])

dict_list = list(capitals)
print(dict_list) # ['Hessen', 'Saarland', 'Baden-Württemberg', 'Rheinland-Pfalz', 'Nordrhein-Westfalen']

print("*" * 30)


#Liste mit sortierten Keys
sorted_capitals = sorted(capitals)
print(sorted_capitals)

print("*" * 30)

# Values iterieren
for city in capitals.values():
    print(city)

print("*" * 30)

# Über Keys und Values iteration
for key, values in capitals.items():
    print(key, ":", values)
