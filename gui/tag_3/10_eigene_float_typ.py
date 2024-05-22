"""
von float erben
"""

class UnitFloat(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value) # hier wird float instanziiert
        instance.unit = unit
        return instance


f = UnitFloat(2, "kg")
print(f, f.unit)