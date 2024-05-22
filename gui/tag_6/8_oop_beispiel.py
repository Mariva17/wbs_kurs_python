"""
Rootklasse
"""

import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry("400x300")  # in pixel


class ControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OOP Ansatz")

        self.set_ui()

    def set_ui(self):
        self.label = tk.Label(self.root, text="das ist ein Label")
        self.label.pack()


if __name__ == "__main__":
    app = ControllerApp(root)
    root.mainloop()
