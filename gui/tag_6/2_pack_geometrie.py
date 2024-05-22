import tkinter as tk

root = tk.Tk()
root.title("Meine erste GUI Anwendung")
root.geometry("800x600") # in pixel


# Widgets
label_1 = tk.Label(master=root, text="Hallo GUI!", bg="yellow")
label_2 = tk.Label(master=root, text="Hallo GUI again!", bg="LawnGreen")
label_3 = tk.Label(master=root, text="Andere GUI!", bg="lightblue")


# Platzieren via Pack-Geometry-Manager
# label_1.pack(side="left", fill="none")  # side: left | right | top | bottom   # fill: x|y|both|none
# label_2.pack(side="right")
# label_3.pack(side="top", fill="x")

label_1.pack(fill="both", pady=10, padx=10, ipady=20)
label_2.pack(fill="both")
label_3.pack(side="left", fill="both", expand=0)




if __name__ == "__main__":
    root.mainloop() 