"""
Klassenvariablen mit Klassenname.Variablenname addressieren.
__del__ wird aufgerufen durch del Keyword oder durch die Garbage Collection
"""


class Robot:
    anzahl = 0

    def __init__(self, name):
        self.name = name
        Robot.anzahl = Robot.anzahl + 1

    def __del__(self) -> None:
        print(f"jetzt wurde ein Roboter gelöscht: {self.name}")
        Robot.anzahl -= 1

c3po = Robot(name="C3PO")
r2d2 = Robot(name="R2D2")
r2d2_clone = r2d2
del r2d2  # veranlasst die GC, __del__ aufzutrufen, wenn refcount = 0

print(Robot.anzahl)

