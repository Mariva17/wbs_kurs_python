"""
Bitshifter GUI

"""
from enum import StrEnum
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from operator import lshift, rshift


SHIFT_VALUES = [1, 2, 3]

class ShiftSymbol(StrEnum):
    LEFT = "<<"
    RIGHT = ">>"


def get_binary_string(n: int) -> str:
    """return binary representation of integer."""
    return f"{n:b}"


def bit_shift(integer_input, shiftby, direction):
    if direction == ShiftSymbol.LEFT:
        return lshift(integer_input, shiftby)
    elif direction == ShiftSymbol.RIGHT:
        return rshift(integer_input, shiftby)
    raise NotImplemented


class BitShifterGui(tk.Tk):
    def __init__(self, title, geometry="800x300"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

        self.shift_by = tk.IntVar()
        self.value_input = tk.IntVar()  # hält den Integer-Input des Users
        self.shift_direction = tk.IntVar()

        self.set_ui()


    def set_ui(self):
        # ---------------------------------
        # LEFT FRAME (INPUT FRAME)
        # ---------------------------------
        
        left_frame = tk.LabelFrame(self, text="Data entry")
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        
        tk.Label(left_frame, text="Input ganzzahlung", font=("Arial", 12)).grid(
           row=0, column=0, padx=10, pady=10 
        )

        tk.Entry(left_frame, textvariable=self.value_input).grid(
            row=0, column=1, padx=10, pady=10, sticky="w"
        )

        tk.Label(left_frame, text="Shift Richtung", font=("Arial", 12)).grid(
           row=1, column=0, padx=10, pady=10 
        )

        shift_dir = ttk.Combobox(left_frame, textvariable=self.shift_direction, width=16)
        shift_dir["values"] = [
            ShiftSymbol.LEFT,
            ShiftSymbol.RIGHT,
        ]

        shift_dir.current(1)  # wählt Index 1 aus als Vorauswahl
        shift_dir.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(left_frame, text="Shift um", font=("Arial", 12)).grid(
           row=2, column=0, padx=10, pady=10 
        )
        shift_by_box = ttk.Combobox(left_frame, textvariable=self.shift_by, width=16)
        shift_by_box["values"] = SHIFT_VALUES
        shift_by_box.grid(row=2, column=1, padx=10, pady=10)
        shift_by_box.current(0)

        # ---------------------------
        # RIGHT FRAME (OUTPUT FRAME)  
        # ---------------------------
        right_frame = tk.LabelFrame(self, text="Data output")
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="news")

        tk.Label(right_frame, text="Binär-Darstellung", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=10 
        )
        self.output_entry = tk.Entry(right_frame)
        self.output_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(right_frame, text="Shifted", font=("Arial", 12)).grid(
            row=1, column=0, padx=10, pady=10, sticky="w" 
        )
        self.shifted_entry = tk.Entry(right_frame)
        self.shifted_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")


        tk.Label(right_frame, text="Dezimal neu", font=("Arial", 12)).grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )

        self.shifted_decimal_entry = tk.Entry(right_frame)
        self.shifted_decimal_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        tk.Button(right_frame, text="Shift it now!", command=self.shift).grid(
            row=3, columnspan=2, pady=20
        )

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def get_decimal_input(self):
        try:
            decimal_input = self.value_input.get()
        except tk.TclError:
            raise ValueError ("Diese Eingabe ist ungültig!")
        if decimal_input < 0:
            raise ValueError("Es nur positive Zahlen erlaubt.")

        return decimal_input


    def shift(self):
        try:
            decimal_input = int(self.value_input.get())
        except ValueError as e:
            messagebox.showerror("Fehlerhafte Eingabe", str(e))
            return

        b = (get_binary_string(decimal_input))
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, b)
        shifted = bit_shift(decimal_input, 2, ShiftSymbol.LEFT)
        print(shifted)

        



if __name__ == "__main__":
    app = BitShifterGui("Bitshifter")
    app.mainloop()




