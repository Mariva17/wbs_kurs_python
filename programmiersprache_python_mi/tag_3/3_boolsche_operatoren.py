"""
and
or
not
"""

# AND (logisches Und)
"""
UND
a       b      a and b
True    True     True
True    False    False
False   False    False
False   True     False
"""

a = True
b = False

if a and b:
    print(" a und b ist wahr")

x = 213
y = 34
z = 3
if x > y and y > z:
    print("wahre Aussage")


"""
OR
a    b    a or b
1    1     1
1    0     1
0    1     1
0    0     0

"""
if x > y or z > y:
    print("wahre Aussage")

if x > y and z < 3 or x > y:
    print("and bindet stärker als or")


a = True
b = False

if a and not b:
    print("a and not b")

a = 12
if 12 <= a <= 24:
    print("a liegt zwischen 12 und 24")


