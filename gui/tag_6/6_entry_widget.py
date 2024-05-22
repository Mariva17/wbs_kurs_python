"""
kleines Formular
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Das Entry Widget")
root.geometry("400x200") 


def say_hello(name):
    print("say hello: ", name)

    # Entry Feld auslesen
    value = entry.get()
    print(value, type(value))

    if len(value) < 2:
        messagebox.showerror("Das Wort ist zu kurz!", "Bitte ein längeres PW eingeben.")
        return
    else:
        messagebox.showinfo("Super!", "Das hast du super gemacht!")

    # Entry Feld löschen
    entry.delete(0, tk.END)

    # Entry Feld einragen
    entry.insert(0, value.upper())


entry = tk.Entry(root)
button = tk.Button(root, text="mein Button", command=lambda: say_hello("Bob"))
button["width"] = 10

entry.pack()
button.pack()


if __name__ == "__main__":
    root.mainloop() 