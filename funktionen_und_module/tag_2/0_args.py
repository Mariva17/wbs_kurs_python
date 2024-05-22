"""
Funktionsparameter und Argumente
Positionelle Argumente
"""


def values(a, b):
    print(a, b)


values(3, 4) # positionelle Argumente

print("*" * 30)
# default-Parameter muss am Ende kommen
# non-default argument follows default argument
def values_mit_default(a, b, c=10):
    print("values_mit_default: ", a, b, c)


values_mit_default(1, 2)
values_mit_default(3, 8, 15)


def values_unbestimmt(a, b, *args):
    # *args kommen am Ende der positionellen Argumente
    print(a, b, args)


values_unbestimmt(1, 2, 6, 7, 8, 9)


def positionelle_args_erzwingen(a, b, /, c):
    # der / sagt aus, dass alles linkes davon muss per Position übergeben werden
    print("positionell erzwingen:", a, b, c)


positionelle_args_erzwingen(100, 200, 300)

# Fehler! b darf nur als position übergeben werden
#positionelle_args_erzwingen(100, b=200, c=300)


