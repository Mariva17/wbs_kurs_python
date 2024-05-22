"""
Typehints: Hinweise auf Datentypen

"""

def summe(a: float, b: float):
    result = a + b
    print("result von summe: ", a + b)


summe(1.1, 2)
# summe("ein", "zwei")
# summe("1", "2")
# summe([1, 2], [2, 3])

user_input = float(input("bitte zahl eingeben: "))
summe(user_input, user_input)
