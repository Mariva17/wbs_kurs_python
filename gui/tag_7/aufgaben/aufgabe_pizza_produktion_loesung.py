from enum import IntEnum, StrEnum
import tkinter as tk


class PizzaSize(IntEnum):
    KLEIN = 1
    MITTEL = 2
    GROSS = 3


class Pizza(StrEnum):
    MARGHARITA = "Margratia"
    CAPRICIOSA = "Capriciosa"
    MARIANA = "Mariana"


def submit():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        print(selected_index)
        print(f"Current Pizza size: {pizza_size_value.get()}")
        print(f"Current Pizza: {selected_item}")
        print("submit")
        print(text.get("1.0", tk.END))


def listbox_select(event):
    selected_index = listbox.curselection()
    selected_item = listbox.get(selected_index)
    print(selected_index)


def create_pizza_choices(frame):
    label_frame = tk.LabelFrame(frame, text="Choose pizza:")
    label_frame.pack(fill="both", expand=True, padx=10, pady=10)
    listbox = tk.Listbox(
        label_frame,
    )
    for idx, pizza in enumerate(Pizza, start=1):
        listbox.insert(idx, pizza)

    listbox.bind("<<ListboxSelect>>", listbox_select)
    listbox.pack(fill="both", expand=True)
    return listbox


def create_pizza_size_frame(frame):
    label_frame = tk.LabelFrame(frame, text="Pizza Größe")
    label_frame.pack(fill="x", expand=True, padx=10, pady=10)

    for size in PizzaSize:
        radio_button = tk.Radiobutton(
            label_frame,
            text=size.name.capitalize(),
            variable=pizza_size_value,
            value=size,
        )
        radio_button.pack(padx=10, pady=5, anchor="w")


root = tk.Tk()
root.title("Pizza Bestellapp Luigi 2000")
root.geometry("800x400")
root.resizable(False, False)

# save the current choosen Pizza size here
pizza_size_value = tk.IntVar()
pizza_style = tk.IntVar()

order_frame = tk.Frame(master=root)
order_frame.grid(row=0, column=0, sticky="new")
create_pizza_size_frame(order_frame)
listbox = create_pizza_choices(order_frame)
button = tk.Button(order_frame, text="Submit", command=submit)
button.pack(expand=True, fill="x")


# REchte Seite Textframe
text_frame = tk.Frame(master=root)
text_frame.grid(row=0, column=1, sticky="news")

label_frame = tk.LabelFrame(text_frame, text="Zusatzinformationen")
label_frame.pack(fill="both", expand=True, pady=15, padx=15)
text = tk.Text(label_frame, height=5, width=40)
text.pack(fill="both", expand=True, pady=15)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=1)

root.mainloop()
