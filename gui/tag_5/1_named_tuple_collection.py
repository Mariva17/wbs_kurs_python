"""
namedtuple aus den collections. (immer noch gebräuchlicher vorhänger von typing.NamedTuple)
(ein benannter Tuple ohne Typehints)

"""
from collections import namedtuple

pen = (2, "Solid", True)

# Problem: man weiß im Code später nicht, was pen[0] sein soll.
if pen[0] > 1 and pen[2]:
    print("Super Stift")

# Anlegen der "Klasse".
# Liste sind die Atttribute
Pen = namedtuple("Pen", "width style beveled")  
pen2 = Pen(width=2, style="Bold", beveled=True)

if pen2.width > 1 and pen2.beveled:
    print("Stift ist breiter als 1 und abgeschrägt")
print(pen2)  # Pen(width=2, style='Bold', beveled=True)

# Tuple als Dict exportieren
print(pen2._asdict())  # {'width': 2, 'style': 'Bold', 'beveled': True}