"""
__repr__ und __str__

__str__ => richtet an sich and den Enduser. Ausgsbe für Programm-Nutzer
__repr__ => interne Repräsentation (für Entwickler)
"""

class Robot:
    def __init__(self, name):
        self.name = name


    def __str__(self) -> str:
        """String-Representation der Robot-Klasse"""
        return self.name


    def __repr__(self) -> str:
        """interne String-Repräsentation. Sollte den Aufruf des Objekts bei Instanziierung nachbilden.
        
        Robot('C3PO')
        """
        return f"Robot(name={self.name!r})"  # !r => __repr__(self.name)

c3po = Robot(name="C3PO")
r2d2 = Robot(name="R2D2")

print(f"{c3po}") # hier wird die String-Representation ausgegeben
print(2) # String-Representation 
print([2, 3, 5, "25"])

robots = [c3po, r2d2]
print(robots)

print("*" * 40)
print(str("Peter"))
print(repr("Peter"))

print("*" * 40)

names = ["Bob", "Alice"]  # "'Bob', 'Alice'"
names_string = ",".join(repr(name) for name in names)
names_string = ",".join(map(repr, names))
print(names_string)


