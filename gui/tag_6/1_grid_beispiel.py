import tkinter as tk

root = tk.Tk()
root.title("Meine erste GUI Anwendung")
root.geometry("800x600") # in pixel


# Widgets
label_1 = tk.Label(master=root, text="Hallo GUI!", bg="yellow")
label_2 = tk.Label(master=root, text="Hallo GUI again!", bg="LawnGreen")


# Platzieren via Pack-Geometry-Manager
label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)



if __name__ == "__main__":
    root.mainloop() 