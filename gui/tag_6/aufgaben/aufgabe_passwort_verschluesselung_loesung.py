import tkinter as tk
from tkinter import messagebox
import hashlib

MAX_LEN = 8
SPECIAL_CHARS = "$%&()?"

root = tk.Tk()
root.geometry("800x200")
root.title("Passwort Verschlüsselung")


def validate(passwort: str) -> None:
    if not passwort:
        raise ValueError("Bitte gebe ein Passwort ein!")

    if len(passwort) < MAX_LEN:
        raise ValueError("Das Passwort ist zu kurz")

    if not any(char.isdigit() for char in passwort):
        raise ValueError("Das Passwort muss mindestens eine Zahl enthalten!")

    if not any(char.isalpha() for char in passwort):
        raise ValueError(
            "Das Passwort muss mindestens einen Buchstaben enthalten!"
        )

    if not any(char in SPECIAL_CHARS for char in passwort):
        raise ValueError(
            "Das Passwort muss mindestens ein Sonderzeichen enthalten!"
        )


def encrypt(passwort) -> str:
    encrypted = hashlib.sha256(bytes(passwort, encoding="utf-8"))
    return encrypted.hexdigest()


def handle_encrypt() -> None:
    passwort = eingabe_entry.get()

    try:
        validate(passwort)
        encrypted = encrypt(passwort)
    except ValueError as e:
        messagebox.showerror("kein Passwort", str(e))
        return

    if not passwort:
        messagebox.showerror("kein Passwort", "Bitte gebe ein Passwort ein!")
        return None

    ausgabe_entry.delete(0, tk.END)
    eingabe_entry.delete(0, tk.END)
    ausgabe_entry.insert(0, encrypted)
    messagebox.showinfo(
        "Erfolgreich!", "Das Passwort wurde erfolgreich verschlüsselt"
    )


# Create a LabelFrame to group elements
labelframe = tk.LabelFrame(root, text="Data Entry")
labelframe.grid(row=0, column=0, padx=10, pady=10, sticky="news")  # responsive


def create_label_entry(frame, text, row):
    name_label = tk.Label(frame, text=text)
    name_label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
    name_entry = tk.Entry(frame, width=70)
    name_entry.grid(row=row, column=1, padx=10, pady=10, sticky="news")
    return name_label, name_entry


eingabe_label, eingabe_entry = create_label_entry(
    labelframe, text="Passwort", row=0
)
ausgabe_label, ausgabe_entry = create_label_entry(
    labelframe, text="verschlüsselt", row=1
)

button = tk.Button(
    labelframe, text="Jetzt verschlüsseln", command=handle_encrypt
)
button.grid(row=2, column=0, padx=10, pady=10)

root.grid_columnconfigure(0, weight=1)
root.mainloop()
