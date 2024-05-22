"""
Aufgabe: Charaktere für ein Roleplaying Game

Definiere eine abstrakte Basisklasse `Character` für Rollenspielcharaktere.
Diese Basisklasse enthält zwei abstrakte Methoden, `attack` und `heal`, die von
abgeleiteten Klassen implementiert werden müssen. Attack und Heal erwarten
einen anderen Character als Argument. Ein Charakter hat einen Namen und eine
Gesundheit (Health), die beim Instanziieren festgelegt wird.

Jede abstrakte Methode ist mit einer Docstring versehen, die erklärt, wofür sie
verwendet wird und welche Argumente sie erwartet. Die Parameter werden mit
Datentypen versehen.

- Es gibt zwei konkrete Klassen, `Warrior` (Krieger) und `Healer` (Heiler), die
  von der abstrakten Basisklasse `Character` erben. Jede dieser Klassen
  implementiert die abstrakten Methoden `attack` und `heal` auf ihre eigene
  Weise.

- Erstelle Instanzen von Krieger und Heiler und demonstrieren deren
  Fähigkeiten, indem wir die `attack`- und `heal`-Methoden aufrufen. Das
  Ergebnis jeder Aktion kann einfach als print() ausgegeben werden.

warrior = Warrior("Boromir", health=100)
healer = Healer("Gandalf", health=80)

warrior.attack(healer, damage=10)  # Krieger greift Heiler an und fügt 10 Schaden zu.
healer.heal(warrior, value=15)    # Heiler heilt Krieger um 15 Gesundheitspunkte.

warrior.heal(healer, value=15)    # ERROR! Ein Krieger hat keine Heilkräfte!
warrior.attack(warrior, damage=10)  # ERROR! Ein Spieler kann sich nicht selbst angreifen

healer.heal(healer, value=15) # Heiler heilt Heiler um 15: Gesundsheitspunkte
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Character(ABC):

  def __init__(self, name, health):
    self.name = name
    self.health = health

  @abstractmethod
  def attack(self, target):
    """Abstract Method
      target = Character - Angriffsziel
    """
    pass
  
  @abstractmethod
  def heal(self, target):
    """Abstract Method
      target = Character - Wer behandelt wird
    """
    pass

class Warrior(Character):

  def attack(self, target: Character, damage: int):
    if target.name == self.name:
      print("ERROR! Ein Spieler kann sich nicht selbst angreifen")
      
    else:
      result = target.health - damage
      return print(f"Krieger {self.name} greift Heiler {target.name} an und fügt {damage} Schaden zu. Dadurch wurde Gesundheitspunkte {target.name}: {result}")

  def heal(self, target: Character, value: int): 
    return print("ERROR! Ein Krieger hat keine Heilkräfte!")


class Healer(Character):
 
  def heal(self, target: Character, value: int):
    if target.name == self.name:
      result = target.health + value
      return print(f"Heiler {self.name} heilt sich selbst um {value} Gesundheitspunkte. Dadurch wurde Gesundheitspunkte {target.name}: {result}")
      
    else:
      result = target.health + value
      return print(f"Heiler {self.name} heilt Krieger {target.name} um {value} Gesundheitspunkte. Dadurch wurde Gesundheitspunkte {target.name}: {result}")
      
  def attack(self, target: Character, damage: int):
    if target.name == self.name:
      print("ERROR! Ein Spieler kann sich nicht selbst angreifen")
    else:
      result = target.health - damage
      return print(f"Heiler {self.name} greift {target.name} an und fügt {damage} Schaden zu. Dadurch wurde Gesundheitspunkte {target.name}: {result}")
      


warrior = Warrior("Boromir", health=100)
healer = Healer("Gandalf", health=80)

warrior.attack(healer, damage=10)  
healer.heal(warrior, value=15) 
print("*"*40)

warrior.heal(healer, value=15)    # ERROR! Ein Krieger hat keine Heilkräfte!
warrior.attack(warrior, damage=10)  # ERROR! Ein Spieler kann sich nicht selbst angreifen
print("*"*40)

healer.heal(healer, value=15)
healer.attack(healer, damage=20)
healer.attack(warrior, damage=10)