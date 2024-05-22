import tkinter as tk
from enum import StrEnum, IntEnum
from abc import ABC, abstractmethod


class State(IntEnum):
    OFF = 0
    ON = 1


class Color(StrEnum):
    OFF = "grey"
    ON = "yellow"


# Define the Switchable interface
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class PowerSwitch:
    def __init__(self, client: Switchable):
        self.client = client
        self.state = State.OFF

    def press(self):
        """Toggle Power state."""
        if self.state:
            self.client.turn_off()
            self.state = State.OFF
        else:
            self.client.turn_on()
            self.state = State.ON


class SwitchableControlApp:
    def __init__(self, root, device: PowerSwitch):
        self.root = root
        self.root.title("Switchable Control")

        self.device = device

        self.label = tk.Label(root, text="OFF", bg=Color.OFF)
        self.label.pack(side="top", fill="both", expand=True)

        self.device_button = tk.Button(root, text="Press", command=self.press)
        self.device_button.pack(pady=10)

    def press(self):
        if self.device:
            self.device.press()
            if self.device.state == State.ON:
                self.label.config(bg=Color.ON, text="ON")
            else:
                self.label.config(bg=Color.ON, text="OFF")


if __name__ == "__main__":
    GUI = True
    if GUI:
        root = tk.Tk()
        root.geometry("300x300")
        lb = LightBulb()
        app = SwitchableControlApp(root, device=PowerSwitch(lb))
        root.mainloop()
    else:
        lb = LightBulb()
        ps = PowerSwitch(client=lb)
        ps.press() # LightBulb: turned on
        ps.press() # LightBulb: turned off
        ps.press() # LightBulb: turned on
