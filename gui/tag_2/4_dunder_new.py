"""
__new__ und __init__ bilden den Konstruktor

"""

class MyClass:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # instance.x = 43
        return instance


    def __init__(self, daten):
        self.daten = daten 


my = MyClass("daten daten daten")
print(my.__dict__)