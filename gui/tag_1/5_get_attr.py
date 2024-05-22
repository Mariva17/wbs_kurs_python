"""

getattr und setattr (Built in Funktionen)

"""

class BananaTree:
    ground = "sandy"

    def __init__(self, bananas):
        self.bananas = bananas
        self.ground = "erde"

tree = BananaTree(bananas=100)
baum = BananaTree(bananas=1000)
BananaTree.x = 128
print("x von baum: ", baum.x)
print("ground von baum: ", baum.ground)

print("Anzahl der Bananen: ", tree.bananas)

# dynamischer Zugriff auf Attribut
user_input = "bananas"
anzahl_bananas = getattr(tree, user_input)
print("Anzahl der Bananen (2): ", anzahl_bananas)

# dem tree-Objekt ein weiteres Attribut dynamisch zuweisen
setattr(tree, "bark", 10)
setattr(BananaTree, "y", 33)

print("*"*40)

# dynamisch Attribute setzen
attr_liste = ["leaves", "roots"]
for attr in attr_liste:
    setattr(tree, attr, 1)

print(tree.__dict__)

print("*"*40)

attr_liste = [("leaves", 2), ("roots", 43)]
for attr, amount in attr_liste:
    setattr(tree, attr, amount)

print(tree.__dict__) # {'bananas': 100, 'bark': 10, 'leaves': 2, 'roots': 43}
print(baum.__dict__) #  {'bananas': 1000}
print(baum.y)