"""
Slider
"""

import tkinter as tk

root = tk.Tk()
double_var = tk.DoubleVar()   # für Python float Werte

def update_label(value):
    print("label wurde upgedated: ", value)


scale = tk.Scale(
    root, variable=double_var,
    from_=0.0,
    to=1.0,
    resolution=0.1,
    orient=tk.HORIZONTAL,
    command=update_label)


scale.pack()

tk.Label(root, textvariable=double_var).pack()



if __name__ == "__main__":

    root.title("Meine erste Listbox")
    root.geometry("800x600")  # in pixel
    root.mainloop()