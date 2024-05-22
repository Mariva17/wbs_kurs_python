"""


"""


class NPC:
    def __init__(self):
        print("wird von Computer gesteuert")

    def walk(self):
        print("wird autogesteuert")


class Human:
    def __init__(self):
        print("ein Mensch")


class Knight(Human):
    def __init__(self):
        # super => Proxy-Objekt und nicht die Klasse!
        super().__init__()
        print("ein Ritter")

    def walk(self):
        print("Ritter bewegt sich")


class Character(Knight, NPC):
    def walk(self):
        super().walk()  # Ritter bewegt sich
        NPC.walk(self)  # wird autogesteuert
        print("Chacter bewegt sich")  # Chacter bewegt sich


c = Character()
c.walk()

print(Character.__mro__)  # Character.mro()