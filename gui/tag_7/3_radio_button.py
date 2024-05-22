"""
Radiobutton

"""

import tkinter as tk


root = tk.Tk()
selected_option = tk.IntVar()
check_state = tk.BooleanVar()
selected_option.set(2)  # Voreinstellung Burger (2)

options = {
    0: "Pizza",
    1: "Salat",
    2: "Burger"
}

def checkbutton_click():
    print("checkbutton wurde geklickt", check_state.get())
    if check_state.get():
        label.config(text="Checkbox wurde aktiviert")
    else:
        label.config(text="Checkbox wurde deaktiviert")



def show_radio_state():
    print(f"Welchen Wert hat die Radio-Group: {selected_option.get()}")
    print(options[selected_option.get()])


# Checkbutton prüfen
print(check_state.get())



for label, value in options.items():
    tk.Radiobutton(root, text=label, variable=selected_option, value=value).pack()


tk.Checkbutton(
    root, text="Aktivier mich!", variable=check_state, command=checkbutton_click
).pack()

label = tk.Label(root, text="Warte auf Aktivierung...")
label.pack()

button = tk.Button(root, text="Show Radio State", command=show_radio_state)
button.pack()




if __name__ == "__main__":

    root.title("Meine erste Radiobutton")
    root.geometry("800x600")  # in pixel
    root.mainloop()