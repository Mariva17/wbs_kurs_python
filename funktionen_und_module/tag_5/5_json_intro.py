"""
Einführung in Json (JavaScript Object Notation)
Austauschformat(plattform- und sprachunabhängig)

Arrays: []
Objekte: {}

"""

import json


data = {
    "member": {
        "name": "Frank Zappa",
        "species": "Human",
        "age": (84, 78), # beim Konvertieren wird ein Json-Array draus
    },
}
print(data)

# Serialisiert einen Python-Objekt
json_data = json.dumps(data) # dumps erzeugt eine json-String
print(type(json_data))
print(json_data)

print("*" * 40)

# Deserialisiert einen Json-Objekt
original_data = json.loads(json_data)
print(original_data)
