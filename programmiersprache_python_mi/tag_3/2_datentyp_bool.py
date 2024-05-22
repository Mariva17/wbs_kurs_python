
"""
Datentyp bool: unverändlich, kennt nur zwei Zustände wahr oder falsh
"""
wahre_aussage = True
unwahre_aussage = False

print(type(unwahre_aussage)) # <class 'bool'>

# Wahrheitswert mit bool erzeugen
x = 42
print("bool(42:)", bool(x))

x = 0
print("bool(0:)", bool(x))

"""
Unwahre Werte:

0, 0.0

[], {}, ()
"""

if True:
    print("das wird ausgeführt, weil  die Aussage wahr ist")

if False:
    print("das wird NIE ausgeführt, weil  die Aussage unwahr ist")    


# Arithmetische vergleichsoperatoren
x = 21
y = 11
print("x > y: ", x > y)

if x > y:
    print("x ist größer als y")

name = ""
# if bool(name)
if name:
    print("Der Name ist: ", name)

name = "Bob"
if name:
    print("Der Name ist: ", name)

# gleiche Variante, nur nicht pythonisch
if len(name) > 0:
    print("Der Name ist: ", name)    

# Operator muss für die Operanden implementiert sein
# if "hamburg" > 4:
#     print("hamburg")