"""
Dict anlegen

"""

# 1. Literal

d = {
    "a": 1,
    "b": 2
}

# 2. Mit Dict Konstruktor
d = dict()
d["a"] = 1
d["b"] = 2

# 3. Mit Dict Konstruktor und Keywordargumente
d = dict(
    name = "Bob",
    age = 34
)
# 4. Mit Liste aus Listen (mit 2 Elementen) 
alphabet_liste = [
    ["A", "aleph"],
    ["B", "beth"]
]
d = dict(alphabet_liste)
print(d)
 