"""
Datentyp set: verändlicher, ungeordnet, iterierbar

"""

# Erzeugen eines Sets
x = set() # leeres Set
y = {} # leeres Dict
z = () # leeres Tuple


x = {"a", "b", "c", "c"}
print(x, type(x)) # doppelte werden gelöscht
print("Länge eines Sets: ", len(x))

# Liste in ein Set konvertrieren
namen = ["Bob", "Alice", "Trudy", "Trudy"]
namen_set = list(set(namen)) # ursprüngliche Reihenfolge bleibt u.U. nicht enthalten
print(namen_set)

# Ein dict umwandeln in ein set
d = {"helium": 7, "oxygen": 3} # beim Dict per Default über Keys iteriert.
d_set = set(d)
print("d_set: ", d_set)


# Basis-Methoden
a = {1, 2, 3, "4", "5", (1,)}
print(a)

# add: ein Element hinzufügen
a.add(8)
a.add(5.0)
a.add(5) # wird nicht eingefügt, da 5.0 enthalten ist
a.add("5") # wird nicht eingefügt, da schon enthalten
print(a)

# remove
a.remove(5)
# a.remove(5) # löst key error aus, da 5 gelöscht wurde
print(a) # {'4', 1, 2, 3, (1,), 8, '5'}

# Discard: ein spezifisches Element löschen
# # Keine Fehlermeldung, wenn nicht enthalten (im Gegensatz zu remove) 
a.discard("nicht enthalten") # löst keinen  error aus

# pop: löscht ein zufälliges element und gibt es zurück
el = a.pop()
print("el: ", el)
print(a)

# update:
a = {1, 2, 3, "4", "5", (1,)} 
b = {66, 88, 57}
c = [1, 2, 3]
d = "abc"
# im  Gegensatz zu Dict lässt set es zu, mehrere Iterables anzuhängen 
a.update(b, c, d)
print(a)

# mit Membership prüfen, ob Element im Set ist
if 2 in a:
    print("ja, 2 ist im set enthalten")

