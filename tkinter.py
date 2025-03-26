

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400) 
canvas.pack()
def hello():
    Label = Label( root, text="Hello World",fg = 'green', font = ("Helvetica", 16, "bold"))
    canvas.create_window(200, 180, window=Label)

button = tk.Button(root, text='Click Me', fg='black' , command= hello )
canvas.create_window(200, 150, window=button)
root.mainloop()