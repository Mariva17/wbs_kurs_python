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
"""MITTEL"""

import tkinter as tk

# root = tk.Tk()
# root.geometry("400x200")
# root.title("Textfeld mit Button")



class Text(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text turn around")
        self.geometry("400x200")
        self.set_ui()


    def set_ui(self):
        labelframe = tk.LabelFrame(self, text="Textfield", border=2, bg="lightblue")
        labelframe.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Input text
        tk.Label(labelframe, text="Text").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.text_input_field = tk.Entry(labelframe)
        self.text_input_field.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Output text
        tk.Label(labelframe, text="Result:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.text_output_field = tk.Entry(labelframe)
        self.text_output_field.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.grid_columnconfigure(0, weight=1) # row 0 in root Grid
        labelframe.grid_columnconfigure(0, weight=1)
        labelframe.grid_columnconfigure(1, weight=6)  # row 1 in labelframe Grid

        # Button
        button = tk.Button(labelframe, text="Read", command=self.button_click)
        button.grid(row=2, column=0, padx=10, pady=10, sticky="w")


    def write_output(self, value):
        """Schreibe Wert in Output Feld"""
        self.text_output_field.config(state="normal")
        self.text_output_field.delete(0, tk.END)
        self.text_output_field.insert(0, value)
        self.text_output_field.config(state="readonly")



    def button_click(self):
        value = self.text_input_field.get()
        result = value[::-1]
        self.write_output(result)





if __name__ == "__main__":
    app = Text()
    app.mainloop() 
