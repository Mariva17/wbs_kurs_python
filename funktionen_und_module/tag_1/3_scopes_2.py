"""
global Keyword (nur in Ausnahmenfällen nutzen)

"""

counter = 6

def old_counter():
    global counter
    counter += 1
    print("lokale Variablen von fn: ", locals())
    

old_counter() # Seiteneffekt!
print("counter global: ", counter)


def better_counter(c):
    c = c + 1
    return c


counter = better_counter(counter) # besser ohne global



def f():
    ...
    print(type(...)) # <class 'ellipsis'> hier als Platzhalter

