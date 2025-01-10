from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry("600x600")

def openNewWindow(title):
    newWindow = Toplevel(root)
    newWindow.title(title)
    newWindow.geometry("400x400")
    Label(newWindow, text=f"{title} átváltás").grid(row=0, column=0, padx=20, pady=20)

label = Label(root, text="Főablak")
label.grid(row=0, column=0, pady=10)

btn1 = Button(root, text="Tömeg átváltás", command=lambda: openNewWindow("Tömeg"))
btn2 = Button(root, text="Hossz átváltás", command=lambda: openNewWindow("Hossz"))
btn3 = Button(root, text="Idő átváltás", command=lambda: openNewWindow("Idő"))
btn1.grid(row=1, column=0, pady=10)
btn2.grid(row=2, column=0, pady=10)
btn3.grid(row=3, column=0, pady=10)
mainloop()