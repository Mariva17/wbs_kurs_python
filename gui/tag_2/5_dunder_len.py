"""
Länge mit len() ermitteln
"""

x = "23541"
print(len(x))



class Value:
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)


    def __len__(self) -> int:
        return len(self.values)


v = Value()
v.add(2)
v.add(45)
print("Länge von v: ", len(v)) # ruft intern __len__() auf!
