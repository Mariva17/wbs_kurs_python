import tkinter as tk

root = tk.Tk()
root.title("Meine erste GUI Anwendung")
root.geometry("800x600") # in pixel

def clicked():
    print("Button click")

button_cnf ={"foreground": "blue"}

# Widgets
label_1 = tk.Label(master=root, text="Hallo GUI!", bg="yellow")
label_2 = tk.Label(master=root, text="Hallo GUI again!", bg="LawnGreen")

button_1 = tk.Button(root, text="Absenden", command=clicked, cnf = button_cnf, bg="white")

# Platzieren via Pack-Geometry-Manager
label_1.pack()
label_2.pack()
button_1.pack()

if __name__ == "__main__":
    root.mainloop() 