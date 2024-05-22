"""(Mittel)
Erstelle eine Passwortverschlüsselungs App mit tkinter

1)
Es werden zwei Eingabefelder benötigt: Eingabe und Output
in Eingabe gibt der User sein Password ein.
in Output wird das verschlüsselte Passwort angezeigt.

Es werden zwei Labels dafür benötigt: "Passwort" und "verschüsselt":

Setze beide Felder und Labels in einen Labelframe.

Bei Klick auf einen Button ("Jetzt verschlüsseln") wird der Wert aus Eingabe
ausgelesen und verschlüsselt. Dann wird der Wert in das Output-Feld 
geschrieben und das Eingabe-Feld wieder gelöscht.

Nutze zum Verschlüsseln des Passworts den sha256 Algorithmus:
import hashlib
encrypted = hashlib.sha256(bytes(passwort, encoding="utf-8"))
encrypted.hexdigest() => verschlüsseltes Passwort in Hexadezimal

2. Zusatzaufgabe
Das zu verschlüsselnde Passwort muss eine Mindestlänge von 8 Zeichen haben.
Es muss aus mindestens einem Buchstaben und einer Zahl bestehen.
Es muss eines der folgenden Zeichen vorkommen: $%&()?

Nutze für die Fehlermeldungen messagebox

from tkinter import messagebox import
messagebox.showError("Fehler!", "Das Passwort ist zu kurz!")

siehe bilder passwort_1 - passwort_3.png
"""

import tkinter as tk
from tkinter import messagebox
import hashlib



class PasswordEncryption(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Encryption")
        self.geometry("600x400")
        self.set_ui()


    def set_ui(self):
        labelframe = tk.LabelFrame(self, text="Data Entry", border=4, bg="lightblue")
        labelframe.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        # Input password
        tk.Label(labelframe, text="Password:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.text_input_field = tk.Entry(labelframe)
        self.text_input_field.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Output password
        tk.Label(labelframe, text="encrypted:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.text_output_field = tk.Entry(labelframe)
        self.text_output_field.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.grid_columnconfigure(0, weight=1) # row 0 in root Grid
        labelframe.grid_columnconfigure(0, weight=1)
        labelframe.grid_columnconfigure(1, weight=6)  # row 1 in labelframe Grid

        # Button
        button = tk.Button(labelframe, text="encrypt now", command=self.button_click)
        button.grid(row=2, column=0, padx=10, pady=10, sticky="w")


    def write_output(self, value):
        """Schreibe Wert in Output Feld"""
        self.text_output_field.config(state="normal")
        self.text_output_field.delete(0, tk.END)
        self.text_output_field.insert(0, value)
        self.text_output_field.config(state="readonly")



    def button_click(self):
        symbols = ["$", "%", "&", "(", ")", "?", "."]
        password = self.text_input_field.get()
        if len(password) < 8:
            messagebox.showerror("No password", "The password is short. It must contains at least 8 symbols.")
        elif "@" not in password:
            messagebox.showerror("No password", "The password is incorrect. It must contain '@'.")
        elif not any(el for el in password if el in symbols):
             messagebox.showerror("No password", "The password is incorrect. It must contain special symbols.")
        elif not any(char.isdigit() for char in password):
            messagebox.showerror("No password", "The password is incorrect. It must contain at least 1 number.")
        elif not any(char.isalpha() for char in password):
            messagebox.showerror("No password", "The password is incorrect. It must contain at least 1 letter.")
        else:
            encrypted = hashlib.sha256(bytes(password, encoding="utf-8"))
            encrypted = encrypted.hexdigest()  # => verschlüsseltes Passwort in Hexadezimal
            self.write_output(encrypted)
            messagebox.showinfo("Successful!", "The password encrypted successful.")

        





if __name__ == "__main__":
    app = PasswordEncryption()
    app.mainloop() 
