import tkinter as tk
from tkinter import filedialog, Text
import proj

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=400, bg="#263D42")
canvas.pack()

button = tk.Button(root, text="Execute", padx=10, pady=5, fg="black", bg="white", command=proj.main)
button.place(width=100, height=30, relx=0.4, rely=0.1)

root.mainloop()