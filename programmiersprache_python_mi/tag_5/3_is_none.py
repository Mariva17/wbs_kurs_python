"""
Datentyp None. Gibts nur einmal im Memory.
Prüfen mit dem Identitätsoperator is.

"""

x = None
y = None

print(id(x), id(y))
x = print()
print(x)

x = 0
x = None

if x is None:
    print("x ist None")

if not x:
    # 0, ", 0.0, None, [], {}, () ...."
    print("not x")

if x is not None:
    print("x ist nicht None")


# x = 1233445566764
# y = 1233445566764
# print(id(x) == id(y))
# print(x is y)