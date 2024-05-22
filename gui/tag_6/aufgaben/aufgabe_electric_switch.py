"""
Aufgabe PowerSwitch (SCHWER)

a) Entwerfe eine TKinter-App, die einen elektischen An-Aus-Schalter repräsentiert.
b) Entwerfe eine Klasse PowerSwitch, die die Methode press() implementiert.
Dieser Methode kann beim Instanziieren ein elektrisches Geräte wie LightBulb
 oder Fan übergeben werden (siehe Bilder electric_switch_1.png und electric_switch_2.png)

Dazu müssen diese Geräte die Methoden turn_on und turn_off
implementieren, die von PowerSwitch.press() aufgerufen wird (in Abhängigkeit,
ob im Powerswitch Strom fliesst oder nicht)

Erzeuge dazu ein Interface Switchable, welches von LightBulb und Fan geerbet
werden. Nutze ABC und abstracte Methoden.

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    ...


class Fan(Switchable):
    ...


class PowerSwitch:
    def __init__(self, c: Switchable):
        ...


class SwitchableControlApp:
    def __init__(self, root, device: Switchable):
        ...


Die Tkinter-App ist eine Klasse, die SwitchableControlApp heisst und
beim Instanzzieren neben dem tkinter-Root Fenster ein Switchable Objekt
übergeben bekommt

lightbulb = LightBulb(Switchable)
switch = PowerSwitch(device=lightbulb)
switch.press() # licht geht an
switch.press() # licht geht aus
switch.press() # licht geht an

fan = Fan(Switchable)
switch = PowerSwitch(device=fan)
switch.press() # Fan geht an
switch.press() # Fan geht aus
...

Beispiel, wie man die Tkinter-App instaziiert:
switch = PowerSwitch(device=lightbulb)
app = SwitchableControlApp(root, device=switch)
root.mainloop()

Es soll auf der commandline ausgegeben werden, ob das Gerät an ist oder nicht.
Die App selbst besteht nur aus einem Button

LightBulb: turned on...
LightBulb: turned off...


Hinweis:
das An- und Ausschalten muss unabhängig von der GUI ebenso klappen.

Fehler!!!!
im Bild electric_switch_2 steht fälschlicherweise "OFF". Dort muss natürlich "ON" stehen.



class SwitchableControlApp:
    def __init__(self, root, device: PowerSwitch):
        ...
"""
