"""
Listbox (Selectbox)
"""

import tkinter as tk
import random


def show_listbox_state(event):
    """Show current selected rows in listbox"""
    current_selected = listbox.curselection()
    selected_item = [listbox.get(index) for index in current_selected]
    print("Aktuell ausgewählt: ", selected_item)


def add_list_item():
    """Füge ein Random item in die Listbox"""
    listbox.insert(tk.END, str(random.random()))


root = tk.Tk()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=14)

listbox.insert(1, "Pizza Salami")
listbox.insert(2, "Pizza Diavola")
listbox.insert(3, "Pizza Funghi")
listbox.bind("<<ListboxSelect>>", show_listbox_state)  # virtueller Event

listbox.pack()

tk.Button(root, text="add list item", command=add_list_item).pack()



if __name__ == "__main__":

    root.title("Meine erste Listbox")
    root.geometry("800x600")  # in pixel
    root.mainloop()

