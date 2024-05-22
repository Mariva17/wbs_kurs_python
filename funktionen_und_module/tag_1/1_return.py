"""
Return Wert

"""

def rauminhalt(a, b, c):
    r = a * b * c
    return r

rauminhalt_1 = rauminhalt(1, 2, 3)
rauminhalt_2 = rauminhalt(1, 2, 3)
print(rauminhalt_1 == rauminhalt_2)
# print(r) Zugriff auf r geht nicht, da r lokal


# Aufgabe
# Schreibe eine funktion calculate_area mit zwei Param. Länge und Breite
# Rückgabewert der Funktion ist die errechnete Fläche
# Falls a oder b <= 0, soll die Funktion 0 zurückgeben. 
# Ansonsten den Flächeninhalt.
# Rückgabewerte der Berechnungen sollen in einer Ergebnis-Liste gespeichert werden

# Aufruf: calculte_area(22, 24.3)
# Ergebnisliste: [534.6, 0, 0.04, 0]

lengths_widths = [(22, 24.3), (-1, 34), (0.2, 0.2), (0, 23)]
    
def calculate_area(länge, breite):
    
    if länge <= 0 or breite <= 0:    
        return 0    
    else:
        return länge * breite
            
           
areas = [f"{calculate_area(a, b):.2f}" for a, b in lengths_widths]
print("areas: ", areas)

#  Schlechter Stil: verschiedene Rückgabe-Datentypen
def fn():
    x = 3
    if x > 2:
        return "hello wert"
    else:
        return 1.2


x = fn()
x.lower()


        
