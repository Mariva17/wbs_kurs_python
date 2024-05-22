"""
Entpacken bei CALL

"""

def summe(a, b):
    print(a, b)


def check(*args, **kwargs):
    print("check arg:" , args)
    print("check kwargs:" , kwargs)


z = (3, 4)

# Zugriff über Index
summe(z[0], z[1]) # unpythonische Variante

# Tupel entpacken
a, b = z
summe(a, b)

# bei call entpacken
# mit einem * => per Position
summe(*z)


t = ["a", 32, 14, 52, 0, 24]
summe(*t[1:3])
check(*t)
print("*" * 30)
# Keyword Arguments

d = {"a": 1, "b": 2} # for ei in d:
check(d)
print("*" * 30)
check(*d) # geht nach args
print("*" * 50)
check(*d.values()) # geht nach args
print("*" * 30)
check(**d)
print("*" * 30) # a=1, b=2 =>werden in den **kwargs aufgesammelt

print("Sortiertes Dict:", sorted(d))
