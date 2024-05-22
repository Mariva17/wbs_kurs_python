"""
Datenklassen lassen sich leicht mit arithmetischen
Vergleichsoperatoren anreichern.

@dataclass(order=True) => liefert arith. Vergleichsoperatoren
@dataclass(frozen=True) => Instanz lässt sich nicht mehr ändern.

"""

from dataclasses import dataclass, field, asdict

@dataclass(order=True, frozen=True)  # , frozen=True
class Robot:
    name: str = field(compare=False)  # raus aus den arith. Vergleichen
    battery: float  # battery: float = 10 => wäre der Defaultwert 10
    speed: float = field(repr=False, default=100.0)

    def hallo(self):
        print(f"Mein Name ist {self.name}")


@dataclass(frozen=True)
class SuperRobot(Robot):
    attack: int = 100


super_robot = SuperRobot("xyz", 20.0, 33, 44)
print("SuperRobot: ", asdict(super_robot))

robots = [
    Robot("R2D2", 90.0, 2.0),
    Robot("C3PO", 95.0, 1.5),
    Robot("XZ1", 10.0, 4),
    Robot("XZ2", 87.0)
]

# Sortiert erst nach Battery, dann nach speed
sorted_robots = sorted(robots)
print(sorted_robots)

# Vergleichoperatoren sind implementiert dank order=True
print(robots[0] == robots[1])
print(robots[0] < robots[1])
print(robots[1] >= robots[0])

for robot in robots:
    print(robot)

# Als dict exportieren
print(asdict(robots[0]))

# geht nicht, wenn @dataclass(frozen=True)
# robots[0].battery = 100

robots[0].hallo()