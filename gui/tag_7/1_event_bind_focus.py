"""
Focus
"""

import tkinter as tk
from functools import partial
from typing import Callable

root = tk.Tk()


def change_tab_order():
    """Reihenfolge der Tabs verändern."""
    entry.focus()
    for wid in [entry2, entry, entry3]:
        wid.lift()


def check(event: tk.Event, a: int, b: int):
    print("ich bin jetzt im focus")
    print(event, type(event))
    print(a, b)


def checkout(event):
    print("ich bin jetzt nicht mehr im focus")


def make_event(a, b) -> Callable:
    def inner(event: tk.Event) -> None:
        print("ich bin jetzt im focus")
        print(event, type(event))
        print(a, b)

    return inner


entry, entry2, entry3 = tk.Entry(root), tk.Entry(root), tk.Entry(root)
entry.pack()
entry2.pack()
entry3.pack()
entry.bind("<FocusIn>", make_event(a=3, b=4))  # umständlich via Closure
# entry.bind("<FocusIn>", partial(check, a=3, b=4))  # partial(event)
# entry.bind("<FocusIn>", check)  # check(event)
entry.bind("<FocusOut>", checkout)

if __name__ == "__main__":

    root.title("Meine erste GUI Anwendung")
    root.geometry("800x600")  # in pixel
    change_tab_order()
    root.mainloop()
