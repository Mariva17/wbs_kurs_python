class LineItem:
    def __init__(self, name):
        self.name = name
        print("Namen der Klasse ausgeben: ", self.__class__.__name__)


x = LineItem("irgendwas")
print("Alle Attribute eines Objekt: ", x.__dict__)
#  oder
print("Alle Attribute eines Objekt: ", vars(x))

# auch alle vererbten Attribute und Methoden
print(dir(x))