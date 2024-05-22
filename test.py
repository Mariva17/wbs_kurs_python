print("hallo welt!")

p = 0x5A3F
x = 23103
print(hex(x))

y = 3
x = (-y)**2
print(x)

s = "the. quick .brown fox"
x = s.rfind(".")
print(x)

names = "Thomas Ingo Meier"
names = "".join(names.split(" "))
print(names)
print(names[-3])

d = {3}
print(type(d))


data = [ [0, 1, 2, 3] for i in range(4) ]
print(data)
print(data[2][0])
# 0

fruit_list = ['Banana', 'Mango', 'Kiwi']
fruit_list1 = fruit_list
fruit_list2 = fruit_list[:]
 
fruit_list1[0] = 'Banana'
fruit_list2[1] = 'Mango'
 
result = 0
 
for i in (fruit_list, fruit_list1, fruit_list2):
    if i[0] == 'Banana':
        result += 1
    if i[1] == 'Mango':
        result += 10
 
print(result) # 33


my_list = [0 for i in range(1, 5)]
print(my_list) # [0, 0, 0, 0]

my_list = [x for x in range(1, 10, 3) if x % 2 == 0]
print(len(my_list)) # 1

x = {(1, 2): 1, (2, 3): 2}
print(x[2, 3]) # 2

user1 = {'name': 'Thomas', 'age': 50}
user2 = user1.copy()
print(id(user1) == id(user2)) # False
print(id(user1))
print(id(user2))

numbers = [1, 2, 3, 4, 5,6,7,8,9]
print(numbers[5:2:-1]) # [6, 5, 4]

def outer(a, b=5):
    def inner(c, d):
        return c + d
    return inner(a, b)
    return a

print(outer(30, 50))

def fn(num):
    return num + 40


num = 3

fn(num)
print(num)

x, y = 10, 0
try:
    result = x / y
except ArithmeticError:
    result = -1
else:
    result = -2

print(result)


spliter = 4 * '+-' + '+'

counter = 0
for x in spliter:
    if x not in spliter:
        counter += 1
print(counter)

data = [1, {}, (2,), (), {3}, [4, 5]]

d = ()  # tuple
c = (2,)  # tuple
a = {3}  # set
b = {}  # dict



class Counter:
    def __init__(self):
        self.count = 0

def increment(c, num):
    c.count += 1
    num += 1
  
counter = Counter()
number = 0
 
for i in range(0, 10):
    increment(counter, number)
 
print(f"Counter is {counter.count}, number is {number}")


class Mitarbeiter:
    def __init__(self, salary=0):
        self.salary = salary


a = Mitarbeiter(100)


class Car:
    def __init__(self, km=32):
        self.km = km
        self.size = '20'
    
 
car1 = Car('20', 32)
car2 = car1

 
print(car1.km)

spliter = 4 * '+-' + '+'

counter = 0
for x in spliter:
    if x not in spliter:
        counter += 1
print(counter)


data = [(0, 1), (1, 2), (2, 3), (3, 4)]
result = sum(i for j, i in data)
print(result)



def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)
    return a

print(outer(50, 30))


