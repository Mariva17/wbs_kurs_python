x = (1, 2, 3, 4)
y = (12, 11, 25, 41)

for i, j in zip(x, y):
    print(i, j)

# per Index zugreifen
print("Element an Index 2:", x[2])
print("Tuple Slicing:", x[0:2], type(x[0:2]))