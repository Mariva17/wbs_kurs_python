"""
mit Frames lassen sich Fenster im Fenster bauen
"""

import tkinter as tk

root = tk.Tk()
root.title("Meine erste GUI Anwendung")
root.geometry("600x400") 

tk.Label(root, text="Outer Label 1", bg="red", fg="white").grid(
    row=0, column=0, sticky="nsew"
)

# einen Rahmen erstellen
frame = tk.Frame(root, bg="gray")
frame.grid(row=1, column=0, sticky="nsew")

button_1 = tk.Button(master=frame, text="hello")
button_1.grid(row=0, column=0, sticky="nsew")
frame.grid_columnconfigure(0, weight=1)
# button_1.pack(side="left") # alternative den Pack-manager nutzen

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    root.mainloop() 