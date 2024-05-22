"""
Enumerate. Für jede Iteration wird ein Tuple zur Verfügung
gestellt, der in der Regel auch gleich entpackt wird.

"""

x = [1, 2, 3]
x_enum = enumerate(x)
print(list(x_enum))

for element in enumerate(x):
    print(element)

# on the fly Entpacken von Werten aus x
for index, value in enumerate(x):
    print(index, value)

