from tkinter import *

root = Tk()
canv = Canvas(root, bg='cyan', width='800', height='800')
b = Button(root, text='Apple').grid(row=1, column=0,)
b2 = Button(root, text='Apple').grid(row=2, column=0,)
canv.grid(row=0, column=0, columns=2,rows=5)

mainloop()
