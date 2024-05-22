id = 3
print(id)

ID = 5
print(ID)

def a():
    return 1

def b(a, b, c=2):
    return print (a, b, c)

b(1, 2)


print((lambda x, y, z: x + y + z)(3, 4, 5))

x = 6
def summe( *, set_val, a=None, b):
    return print(a, b, set_val)

summe(a=12, b=1, set_val="OV")

def fn(a, b):
    print(a)
    


x = '\''
print(len(x),"skhlshlkhn")



class Cat:
    Species = 1
 
    def get_species(self):
        return 'kitty'
 
 
class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
 
    def set_species(self):
        pass
 
 
creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))


foo = [i + i for i in range(5)]
print(foo)


x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)


import math
import random
 
result = math.e != math.pow(2, 4)
print(int(result))



def main(a, b, c, d):
    value = a + b * c - d
    return value

print(main(1, 2, 3, 4))
