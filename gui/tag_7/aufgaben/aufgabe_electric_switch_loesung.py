import tkinter as tk
from tkinter import messagebox
from enum import StrEnum, IntEnum
from abc import ABC, abstractmethod


class State(IntEnum):
    OFF = 0
    ON = 1


class Color(StrEnum):
    OFF = "grey"
    ON = "yellow"


def switchable_factory(device_name: str):
    if device_name == "Lightbulb":
        return LightBulb()
    if device_name == "Fan":
        return Fan()
    raise NotImplementedError("This Device is not available!")


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
    def __init__(self, client: Switchable | None = None):
        self.client = client
        self.state = State.OFF

    def press(self):
        if self.client:
            if self.state == State.ON:
                self.client.turn_off()
                self.state = State.OFF
            else:
                self.client.turn_on()
                self.state = State.ON


# Create a Tkinter GUI for controlling switchable devices
class SwitchableControlApp(tk.Tk):
    def __init__(self, device: PowerSwitch):
        super().__init__()
        self.geometry("300x300")
        self.title("Switchable Control")

        self.device = device

        # Device Label
        self.device_list_label = tk.Label(
            self, text="List of available devices:", bg="green"
        )
        self.device_list_label.pack(fill="x")

        # Device List box
        self.select_box = self.load_devices_list()
        self.select_box.pack(fill="x")

        # Licht
        self.label = tk.Label(self, text="OFF", bg=Color.OFF)
        self.label.pack(side="top", fill="both", expand=True, pady=20)

        # ON OFF BUTTON
        self.device_button = tk.Button(self, text="Press", command=self.press)
        self.device_button.pack(pady=10)

    def listbox_select(self, event):
        selected_index = self.select_box.curselection()
        selected_item = self.select_box.get(selected_index)
        messagebox.showinfo("you choose", f"You have choosen: {selected_item}")
        try:
            self.device.client = switchable_factory(selected_item)
            self.plug_in()
        except NotImplementedError as e:
            messagebox.showerror("Ein Fehler ist aufgetreten!", str(e))

    def load_devices_list(self):
        listbox = tk.Listbox(self, height=2)
        for i, item in enumerate(["Lightbulb", "Fan"], start=1):
            listbox.insert(i, item)

        listbox.bind("<<ListboxSelect>>", self.listbox_select)
        return listbox

    def toggle_background(self):
        if self.device.state:
            self.label.config(bg=Color.ON, text="ON")
        else:
            self.label.config(bg=Color.OFF, text="OFF")

    def plug_in(self):
        print(f"Device: {self.device.client} is plugged in!")
        self.device.state = State.OFF
        self.toggle_background()

    def press(self):

        if self.device.client:
            self.device.press()
            self.toggle_background()
        else:
            messagebox.showerror(
                "Kein Gerät geladen", "Es wurde bisher kein Gerät geladen!"
            )


if __name__ == "__main__":

    app = SwitchableControlApp(device=PowerSwitch())
    app.mainloop()
