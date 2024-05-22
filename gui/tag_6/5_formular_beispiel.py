"""
kleines Formular
"""

import tkinter as tk

root = tk.Tk()
root.title("Kleine Formularanwendung")
root.geometry("800x600") 

# Labelframe: ein Frame mit Überschrift
labelframe = tk.LabelFrame(root, text="User Information", border=2)
labelframe.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


def read_input():
    name_text = user_entry.get() # den Wert des Name-Entry Feldes holen
    prof_text = prof_entry.get()
    print(name_text, prof_text)


def create_label_entry(frame, text, row):
    name_label = tk.Label(frame, text=text)
    name_label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
    name_entry= tk.Entry(frame)
    name_entry.grid(row=row, column=1, padx=10, pady=10, sticky="news")

    return name_label, name_entry

user_label, user_entry = create_label_entry(labelframe, "Username", 0)
prof_label, prof_entry = create_label_entry(labelframe, "Profession:", 1)
button = tk.Button(labelframe, text="Submit", command=read_input)
button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

root.grid_columnconfigure(0, weight=1) # row 0 in root Grid
labelframe.grid_columnconfigure(0, weight=1)  # row 0 in labelframe Grid
labelframe.grid_columnconfigure(1, weight=4)  # row 1 in labelframe Grid


if __name__ == "__main__":
    root.mainloop() 