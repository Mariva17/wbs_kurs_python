"""
Tiefe Kopie: Good Practice: immer wenn man Listen kopiert, deepcopy nutzen

"""

from copy import deepcopy

m = [1, 2, 3, 4, [42]]
m_copy = deepcopy(m)
m[0] = 99
m[4].append(11)
print(id(m))
print(id(m_copy))

print(m)
print(m_copy)

# Seiteneffekt
def fn(arg):
    arg.append(2)

fn(m)
print(m)