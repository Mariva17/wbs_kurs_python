"""
[]-Syntax => a.__getitem__(index) a.__setitem__(index, value)

values = [2, 4]
values[0] => hier wird __getitem__ aufgerufen
values[0] = 1 => hier wird __setitem__ aufgerufen
"""

class Example:
    def __setitem__(self, index, name):
        print(index, name)

x = Example()
x[2, 2] = "Hamburg" # x.__setitem__(index, name)
print("*" * 40)

class Building:
    """Zugriff via obj[index]."""
    def __init__(self, floors):
        self._floors = [None] * floors


    def __setitem__(self, index, name):
        self._floors[index] = name

    def __getitem__(self, index):
        return self._floors[index]



class BuildingOld:
    def __init__(self, floors):
        self._floors = [None] * floors


    def occupy(self, index, name) -> None:
        self._floors[index] = name


    def get_floor_data(self, index) -> str | None:
        return self._floors[index]


building_old = BuildingOld(floors=4)
building_old.occupy(0, "Reception")
building_old.occupy(2, "ABC Corp.")
print(building_old.get_floor_data(2))

print("*" * 40)

# mit __getitem__ und __setitem__
building = Building(floors=4)
building[0] = "Reception"
building[2] = "ABC Corp."
print(building[0])

