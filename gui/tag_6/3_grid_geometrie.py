import tkinter as tk

root = tk.Tk()
root.title("Meine erste GUI Anwendung")
root.geometry("800x600") # in pixel



label_1 = tk.Label(master=root, text="Hallo GUI!", bg="yellow")
label_2 = tk.Label(master=root, text="Hallo GUI again!", bg="LawnGreen")
label_3 = tk.Label(master=root, text="down under!", bg="blue")


# Platzieren via Pack-Geometry-Manager
label_1.grid(row=0, column=0, sticky="news")
label_2.grid(row=0, column=1, sticky="news")
label_3.grid(row=1, column=0, sticky="news")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

if __name__ == "__main__":
    root.mainloop() 