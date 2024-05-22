"""(MITTEL)
Erstelle eine App, in der die Angestellen eines Pizza-Lieferdienstes 
eine Pizza konfigurieren können und beim Absenden werden die Daten auf der 
Konsole ausgegeben.


Folgende Felder müssen implementiert sein:

- Pizza-Variante (als Listbox, zb. Neapolitana, Venezia, Marianara, ...)
- gross / mittel / klein (Radiobuttons)

Zusatzaufgabe:
Es soll zusätzlich über ein Textfeld (Textwidget) möglich sein, 
Informationen zur Bestellung hinzuzufügen.

siehe Bild pizza_produktion.png
"""
import tkinter as tk


class Order(tk.Tk):
    options = {"Klein": 0, "Mittel": 1, "Gross": 2}
    pizza_options = {1:"Margarita", 2: "Hawaii", 3: "Salami", 4: "Diavolo", 5: "Special", 6: "Veggy", 7: "Pepperoni"}

    def __init__(self, title, geometry="800x300"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.selected_option = tk.StringVar()
        self.order = []

        self.set_ui()

    def check_submit(self):
        item_pizza = self.listbox.curselection()
        if not item_pizza:
            print("Please make your choise!")
        else:
            pizza = self.pizza_options[item_pizza[0]]
            size_pizza = self.options[self.selected_option.get()]

            pizza_tuple = (pizza, size_pizza)
            self.order.append(pizza_tuple)


    def set_ui(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Choose Pizza - Frames
        left_frame = tk.LabelFrame(self, text="Pizza size")
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="news")

        frame = tk.Frame(left_frame)
        frame.pack(side="left")
        
        
        for label, value in self.options.items():
            tk.Radiobutton(frame, text=label, variable=self.selected_option, value=value).pack(pady=5)

        left_frame2 = tk.LabelFrame(self, text="Choose Pizza")
        left_frame2.grid(row=1, column=0, padx=20, pady=20, sticky="news")

        self.listbox = tk.Listbox(left_frame2, selectmode=tk.MULTIPLE, height=5)
        scrollbar = tk.Scrollbar(left_frame2)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        for index, label in self.pizza_options.items():
            self.listbox.insert(index, label)

        self.listbox.pack(side="left", fill="both")
        scrollbar.pack(side="right", fill="both")

        # Button
        button = tk.Button(self, text="Submit", command=self.check_submit)
        button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Info Frame
        frame_info = tk.LabelFrame(self, text="Information").grid(
            row=0, column=1, padx=10, pady=10, sticky="news")
        self.info = tk.Text(frame_info, ).grid(row=0, column=1, padx=10, pady=10, sticky="news")
        # pack(fill="both", expand=True)
        frame = tk.Frame(left_frame)
        frame.pack(side="left")







            
            


            





if __name__ == "__main__":

    app = Order("Order Pizza")
    app.mainloop()


        

