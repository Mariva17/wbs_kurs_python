"""
Verzweigung mit IF ELSE

"""

city = "Hamburg"

if city and city[0] == "H" and city[-1] == "g":
    print("City fängt mit großem H an")
else:
    print("City fängt mit NICHT großem H an")


# pythonische Variante
if city.startswith("Ha") and city.endswith("g"):
    print("City fängt mit großem H an")
else:
    print("City fängt mit NICHT großem H an")

"""
elif (else if)
"""

geburtsort = "Hamburg"
if geburtsort == "Hamburg":
    print("in HH geboren")
elif geburtsort == "Berlin":
    print("in B geboren")
elif geburtsort == "Bonn":
    print("in B geboren")    
else:
    print("woanders geboren")


x = 34

if x < 100:
    print("x ist kleiner als Schwellenwert")
if x < 78:
    print("x ist kleiner als 78")
else:
    print("x ist größer als 78")    


age = 18
if age > 18:
    if age > 21:
        print("größer 21")
    else:
        print("kleiner 21")    
elif age > 16:
    print("age ist > 16")
else:
    print("anderes alter")        