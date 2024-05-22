"""
setattr (Schwer)
Wir haben eine Klasse LineItem gegeben. Erstelle LineItem-Objekte und speichere
sie in einer Liste line_items. Achte in __init__ darauf, dass die Werte in
**kwargs übergeben werden und erstelle dynamisch die Attribute.
Es muss __repr__ implementiert sein, __exakt__ wie unten gezeigt.
"""


class LineItem:
    def __init__(self, **kwargs):
        ...

    def __repr__(self):
        ...


lines = [
    {"id": 3, "name": "Pencil Geha", "style": "bold", "color": "black"},
    {
        "id": 13,
        "name": "Pencil Geha Professional",
        "style": "bold",
        "color": "red",
    },
    {
        "id": 23,
        "name": "Parker Chef",
        "style": "thin",
        "color": "silver",
    },
]

line_items = []
print(line_items)
# Result:
# [<LineItem(id=3,name='Pencil Geha',style='bold',color='black')>, <LineItem(id=13,name='Pencil Geha Professional',style='bold',color='red')>, <LineItem(id=23,name='Parker Chef',style='thin',color='silver')>]
