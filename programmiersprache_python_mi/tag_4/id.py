
fruits = ["apple", "cherry", "banana"] 
name = ["Bob", "Alice", "Trudy"]
print(id(fruits))
print(id(name))

if fruits is name:
    print("ist nicht fall")
else:
    print("es handelt sich nicht um das gleiche Objekt")


x = 3
print(f"{id(x)=}")

x = 4
print(f"{id(x)=}")