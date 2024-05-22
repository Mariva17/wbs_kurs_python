"""

Two-Way-Binding mit StringVar (Synchronisieren von Variable und Widget-Wert)

""" """
Einen Maus-Move Event an ein Label binden


"""

import tkinter as tk


root = tk.Tk()
string_var = tk.StringVar()
string_var.set("Initial Value")


entry = tk.Entry(root, textvariable=string_var)
label = tk.Label(root, textvariable=string_var)

entry.pack()
label.pack()

if __name__ == "__main__":

    root.title("Meine erste Stringvar")
    root.geometry("800x600")  # in pixel
    root.mainloop()