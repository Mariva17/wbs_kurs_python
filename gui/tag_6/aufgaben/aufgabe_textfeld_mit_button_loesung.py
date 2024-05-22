import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Textfeld mit Button")


def print_output():
    value = eingabefeld.get()
    print(value)
    ausgabefeld.config(state="normal")
    eingabefeld.delete(0, tk.END)
    ausgabefeld.delete(0, tk.END)
    ausgabefeld.insert(0, value[::-1])
    ausgabefeld.config(state="readonly")


labelframe = tk.LabelFrame(root, text="User-Eingabe")
labelframe.grid(row=0, column=0, padx=10, pady=10, sticky="news")

# Eigabe
label = tk.Label(labelframe, text="Eingabe")
label.grid(row=0, column=0, padx=10, pady=10)
eingabefeld = tk.Entry(labelframe)
eingabefeld.grid(row=0, column=1, padx=10, pady=10)

# Ausgabe
label_2 = tk.Label(labelframe, text="Ausgabe")
label_2.grid(row=1, column=0, padx=10, pady=10)
ausgabefeld = tk.Entry(labelframe)
ausgabefeld.grid(row=1, column=1, padx=10, pady=10)

# Button
button = tk.Button(labelframe, text="Submit", command=print_output)
button.grid(row=2, column=0, padx=10, pady=10)

print(button.keys())

root.grid_columnconfigure(0, weight=1)
root.mainloop()
