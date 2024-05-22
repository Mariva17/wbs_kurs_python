"""
Übergabe an Funktion

"""


def fn(x, y):
    print("id von x in Funktion: ", id(x))
    print(x)
    x = x + 1
    print("id von x in Funktion: ", id(x))

    print("id von y in Funktion: ", id(y))
    y.append("c") # Seiteneffekt!


x = 3
y = ["a", "b"]
print("id von x global: ", id(x))
fn(x, y)

print("Ergrbnis: ", x)
print("Ergrbnis: ", y)


value_dict = {"a": 1, "b": 2}

# Wenn ursprünglicher (veränderlicher Wert) nicht verändert soll
# vor der Operation eine Kopie anlegen
def add_number(value_dict, value):
    value_dict = value_dict.copy() # !shallow copy
    for key in value_dict:
        value_dict[key] += value
    return value_dict


added_dict = add_number(value_dict, 3)
print(added_dict, id(added_dict))
print(value_dict, id(value_dict))
