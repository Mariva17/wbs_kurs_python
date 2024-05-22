"""(Einfach)
Erstelle eine kleine TKinter-App mit einem Labelframe ("Usereingabe").

1)
Setze ein Label (tk.Label) und ein Eingabefeld (tk.Entry) in das Labelframe.
Setze darunter einen Button. Bei klick auf Button soll das Textfeld
ausgelesen werden und in der STandard-Ausgabe mit print ausgegeben werden
Nutze den Grid-Layout-Manager.


2) (Mittel)
Zusatzaufgabe: Gebe die Eingabe in einem Ausgabe-Textfeld aus. Lege dazu
im Labelframe ein weiteres Label und ein weiteres Eingabefeld (tk.Entry) an.
Die Eingabe soll umgedreht (reversed) ausgegeben werden.
Das Ausgabefeld soll readonly sein (state="readonly").
Dazu muss der State des Entry-Fields auf readonly gesetzt werden.
Da allerdings nichts in ein Readonly-Feld geschrieben werden kann, muss
es für den Shreibvorgang kurz auf state=normal gesetzt werden()

def write_field():
    ausgabefeld.config(state="normal") # zum Schreiben muss state=normal sein
    ausgabefeld.insert(0,...)
    ausgabefeld.config(state="readonly")


"""

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Textfeld mit Button")


labelframe = tk.LabelFrame(root, text="Textfield", border=2, bg="lightgreen")
labelframe.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

def read_text():
    value = user_entry.get()
    print(value)
    


def create_label_entry(frame, text, row):
    name_label = tk.Label(frame, text=text)
    name_label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
    name_entry= tk.Entry(frame)
    name_entry.grid(row=row, column=1, padx=10, pady=10, sticky="nsew")

    return name_label, name_entry


user_label, user_entry = create_label_entry(labelframe, "Text", 0)
button = tk.Button(labelframe, text="Read", command=read_text)
button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

root.grid_columnconfigure(0, weight=1) # row 0 in root Grid
labelframe.grid_columnconfigure(1, weight=4)  # row 0 in labelframe Grid


if __name__ == "__main__":
    root.mainloop() 
