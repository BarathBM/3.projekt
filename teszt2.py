from tkinter import *
from tkinter.ttk import *

master = Tk()

master.geometry("600x600")

def openNewWindow(title):
    newWindow = Toplevel(master)
    newWindow.title(title)
    newWindow.geometry("400x400")
    Label(newWindow, text=f"This is {title}").grid(row=0, column=0, padx=20, pady=20)

label = Label(master, text="This is the main window")
label.grid(row=0, column=0, pady=10)

btn1 = Button(master, text="Click to open Window 1", command=lambda: openNewWindow("Tomeg"))
btn2 = Button(master, text="Click to open Window 2", command=lambda: openNewWindow("Hossz"))
btn3 = Button(master, text="Click to open Window 3", command=lambda: openNewWindow("Ido"))
btn1.grid(row=1, column=0, pady=10)
btn2.grid(row=2, column=0, pady=10)
btn3.grid(row=3, column=0, pady=10)
mainloop()