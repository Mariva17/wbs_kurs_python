"""
Set als Key eines Dicts nutzen

"""
d = {}
x = set([1, 2, 3])
# d[x] = 3 # TypeError: unhashable type: "set"

# Ein Frozenset ist ein unverändedrliches Set, welches als
# Key eines Dicts genutzt werden kann
x = frozenset([1, 2, 3])
print(type(x))
d[x] = "Hamburg"
print("Dict d:", d)
print(d.get(frozenset([1, 2, 3]))) # Hamburg

# Frozenset kann somit als Element eines set genutzen werden
y = set([x, frozenset([11, 12, 123])])
print(y)