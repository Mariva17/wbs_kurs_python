"""
PCAP - Wissen: sort und sorted

"""

rabbits = [
    "fiver34",
    "hazel29",
    "bigwig89",
    "blackberry32",
    "buckthorn23",
    "dandelion21",
    "pipkin99",
    "silver22",
    "corn23",
    "hawkbit02",
    "speedwell99",
    "strawberry21",
]

# Inplace-Sortierung und hat keinen Rückgabewert
rabbits.sort() # Rückgabewert ist None  - rabbits = rabbits.sort() FEHLER!
print("rabbits_sorted: ", rabbits)

# erzeugt eine neue Liste! und muss einer Variablen zugewiesen werden
numbers = [34, 24, 1, 68, 8]
sorted_list = sorted(numbers)
print("sorted:", sorted_list)
print(numbers)
