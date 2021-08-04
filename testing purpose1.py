from tkinter import *

def changed():
    size = label.grid_info().get("row") #getting current row
    if size == 0:size = 1
    elif size == 1:size = 0
    label.grid(row=size,column=0)
root = Tk()
root.config(bg="pink")
frame = Frame(root, bg="sky blue")
frame.pack()

label = Label(frame,text="Hello")
label.grid(row=0,column=0)
b = Button(frame, text='Press me!', command=changed)
b.grid(row=0, column=1)

root.mainloop()