
"""
CM to M Umrechner
"""
import tkinter as tk
from tkinter import messagebox


def calculate(cm: int) -> float:
     """Rechne cm nach m."""
     return cm / 100 


class Umrechner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cm nach Meter Umrechner")
        self.geometry("400x200")
        self.set_ui()

    def set_ui(self):
        """Set widgets for calculator."""
        frame = tk.LabelFrame(self, text="Umrechnen von cm in m")
        frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)

        # Eingabe von cm
        tk.Label(frame, text="CM eingeben").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.cm_input_field = tk.Entry(frame)
        self.cm_input_field.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Ausgabe von m
        tk.Label(frame, text="Meter:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.m_output_field = tk.Entry(frame)
        self.m_output_field.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Button
        button = tk.Button(frame, text="Submit", command=self.button_click)
        button.grid(row=2, column=2, padx=10, pady=10, sticky="e")


    def write_output(self, value):
        """Schreibe Wert in Output Feld"""
        self.m_output_field.config(state="normal")
        self.m_output_field.delete(0, tk.END)
        self.m_output_field.insert(0, value)
        self.m_output_field.config(state="readonly")



    def button_click(self):
        try:
            value = int(self.cm_input_field.get())
        except ValueError as e:
            messagebox.showerror(
            "Fehler in der Eingabe!",
            "Es wurde ein ungültiger Wert eingegeben."
            )
            print(e)
            return
        if value < 0:
            messagebox.showerror(
            "Fehler in der Eingabe!",
            "Es wurde ein ungültiger Wert eingegeben."
            )
            return

        m = calculate(value)
        self.write_output(m)




if __name__ == "__main__":
    app = Umrechner()
    app.mainloop()


"""


import tkinter as tk

# root = tk.Tk()
# root.title("Kleine Formularanwendung")
# root.geometry("800x600")  # in pixel


def calculate(cm: int) -> float:
"""    """Rechne cm nach m.""" """
    pass


class Umrechner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cm nach Meter Umrechner")
        self.geometry("400x200")
        self.set_ui()

    def set_ui(self):
    """     """Set widgets for calculator.""" """
        frame = tk.LabelFrame(self, text="Umrechnen von cm in m")
        frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)

        # EINGABE von cm
        tk.Label(frame, text="CM eingeben:").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.cm_input_field = tk.Entry(frame)
        self.cm_input_field.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # AUSGABE von m
        tk.Label(frame, text="Meter:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.m_output_field = tk.Entry(frame, state="readonly")
        self.m_output_field.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Button
        button = tk.Button(frame, text="Submit", command=self.button_click)
        button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def button_click(self):
        calculate(30)
        print("button wurde geklickt")


if __name__ == "__main__":
    app = Umrechner()
    app.mainloop()


"""