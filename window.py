from tkinter import *

root = Tk()
root.title("Window 1")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")

def open_win():
    top = Toplevel()
    top.title("Window 2")
    top.iconbitmap("C:/Users/borbe/Pictures/code.ico")
    label = Label(top, text="Hello").pack()
    button_2 = Button(top, text="close window", command=top.destroy).pack()

button = Button(root, text="open 2nd window", command=open_win).pack()


mainloop()
