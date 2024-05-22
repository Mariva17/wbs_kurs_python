"""
Gegeben sind zwei Dicts, a und b
Erstelle ein neues Dict, dass nur Keys enthält, die in beiden
dicts vorkommen.
der Key dieses neuen Dicts ist jeweils der Key, der Value ist
ein Tupel aus den Werten der Ursprungsdicts.

a = {"a": 1, "b": 2, "z": 3, "c": 4}
b = {"a": 4, "b": 4, "c": 43, "s": 3}

c = {'c': (4, 43), 'a': (1, 4), 'b': (2, 4)}
"""
a = {"a": 1, "b": 2, "z": 3, "c": 4}
b = {"a": 4, "b": 4, "c": 43, "s": 3}
c = {}


k = set(list(a.keys()) + list(b.keys()))

for x in k:
    v1 = a.get(x)
    v2 = b.get(x)
    if v1 == None:
        continue
    elif v2 == None:
        continue
    else:
        v = (v1, v2)
    c[x] = v

print(c)    