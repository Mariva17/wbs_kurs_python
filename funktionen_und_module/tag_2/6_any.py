"""
Built-in Funktionen: all und any

hier: any

"""

# d.h. als wahr evaluiert, wenn ein Element des Iterables wahr ist
x = [0, 1, 1]
print(any(x)) # True




# Aufgabe: prüfe, ob in der Liste ein String enthalten ist, der uppercase ist.
# str.isupper()
# nutze dazu any und list comprehensions
string_list = ["aaa", "ABC", "abc"]

result = any([el.isupper() for el in string_list])
print("Die Liste enthält einen uppercase String:" if result else "Die Liste enthält keinen uppercase String.")


