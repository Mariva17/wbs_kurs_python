"""
Globaler und lokaler Geltungsbereich (scope)

"""
x = 1
z = 12

def fn():
    z = 1
    print(z) # z ist im lokalen Scope definiert. Shadowing (Überschatten) 
    print("lesender Zugriff auf x aus globalem Scope:  ", x)
    print("lokaler Scope von fn: ", locals())

fn()

print(globals()) # erzeugt ein Dict mit globalen Variablen
# print(z)  NameError, z ist nur im lokalen Scope von fn definiert

print(f"{z=}")