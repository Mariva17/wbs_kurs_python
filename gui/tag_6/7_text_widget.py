import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Das Entry Widget")
root.geometry("400x300") 

def read_text_field():
    content = text.get("1.1", tk.END)  # 1.Zeile, 1.Zeichen
    print(content)
    label.config(text=f"Eingegebener Text:\n{content}")


frame = tk.Frame(root, background="grey")
frame.pack()

label = tk.Label(frame, text="")
label.pack()


text = tk.Text(frame, height=5, width=30)
text.pack()

button = tk.Button(frame, text="Read Text", command=read_text_field)
button.pack()

if __name__ == "__main__":
    root.mainloop() 