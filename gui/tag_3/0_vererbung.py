"""
Vererbung

"""

class Tier:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return "bbla blubb"


dog = Tier(name="Fiffi")
katze = Tier(name="Tom")
print(dog.__str__())