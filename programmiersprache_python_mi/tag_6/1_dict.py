"""
Datentyp Dict
"""

d = {} # leeres Dict

d = {"a": 1, "b": [2, 2]}

en_de = {
    "house": "Haus",
    "cat": "Katze",
    "black": "schwarz"
}
print(type(en_de)) # <class 'dict'>

# Zugriff auf ein Element von Dict
print(en_de["house"])

en_de = {
    "house": ["Haus", "Wohnung"],
    "cat": "Katze",
    "black": "schwarz",
    # ["x", "y"]: "z" # geht nicht, weil Liste ein verändlicher Wert ist
    # 0: 3
    # (2, 3): "kfsksks" # das geht
}

# Prüfen, ob key enhalten ist, und falls ja, ausgeben
if "cat" in en_de:
    print(en_de["cat"])

# en_de["blacki"]
# Oder man nutzt die get-Methode des dict
# als zweites Argument von get kann der Defaultwert angegeben werden
result = en_de.get("blacki", 42)
print(result)