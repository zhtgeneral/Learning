import numpy as np
import tkinter as tk

root = tk.Tk()
root.title("Python app")

def enter():
    label.configure(text="Name: " + entry.get())

frame = tk.Frame(root, width=466, height = 333)
frame.pack()

label = tk.Label(frame, text="Enter Name: ")
entry = tk.Entry(frame)
button = tk.Button(frame, text="Enter", command=enter)

label.grid()
entry.grid()
button.grid()

root.mainloop()

#say main is updated

