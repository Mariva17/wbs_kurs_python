"""
Einen Maus-Move Event an ein Label binden
"""

import tkinter as tk

root = tk.Tk()


def print_position(event) -> None:
    """Print x and y coordinates of mouse pointer."""
    print(f"{event.x=} / {event.y=}")


def hello(event) -> None:
    print("HELLO!")


label_1 = tk.Label(master=root, text="hallo gui!", bg="red")
label_1.pack(ipadx=30, ipady=30)
label_1.bind("<B1-Motion>", print_position)  # Motion mit ButtonClicked
label_1.bind("<Button-1>", hello)

if __name__ == "__main__":

    root.title("Meine erste GUI Anwendung")
    root.geometry("800x600")  # in pixel
    root.mainloop()
