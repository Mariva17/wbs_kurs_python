"""
Erweitere die Aufgabe vom Vortag (Schwer)
Beim Instanzieeren der SwitchableControlApp soll zwar ein PowerSwitch-Objekt
übergeben werden, allerdings ist diesem Powerswitch noch kein Gerät zugeordnet
(Lightbulb, Fan)

Die Auswahl des Geräts soll über eine Tkinter-Listbox ermöglicht werden.
Dazu muss bei Auswahl aus einer Liste von möglichen Geräten dem
powerswitch-Objekt ein Switchable-Gerät (zb. Fan) zugeordnet werden können.


# eine App erstellen mit root-Window und leerem Powerswitch
app = SwitchableControlApp(root, device=PowerSwitch())


Hier lässt sich gut eine Factory nutzen:

def switchable_factory(device_name: str):
    if device_name == "Lightbulb":
        return LightBulb()
    ... 

    raise NotImplementedError("This Device is not available!")

siehe Bilder electric_switch
"""
