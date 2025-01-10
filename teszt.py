from tkinter import *
from tkinter.ttk import *

root = Tk()
 

root.geometry("200x200")
 
 

def openNewWindow():
     
    
    newWindow = Toplevel(root)
 
    
    newWindow.title("New Window")
 
    
    newWindow.geometry("200x200")
 
    
    Label(newWindow, 
          text ="This is a new window").pack()
 
 
label = Label(root, 
              text ="This is the main window")
 
label.pack(pady = 10)
 

btn = Button(root, 
             text ="Click to open a new window", 
             command = openNewWindow)
btn.pack(pady = 10)
 

mainloop()