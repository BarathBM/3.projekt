from tkinter import *
from tkinter.ttk import *

master = Tk()
 

master.geometry("600x600")
 
 

def openNewWindow():
     
    
    newWindow = Toplevel(master)
 
    
    newWindow.title("New Window")
 
    
    newWindow.geometry("400x400")
 
    
    Label(newWindow, 
          text ="This is a new window").pack()
 
def openNewWindow2():
     
    
    newWindow = Toplevel(master)
 
    
    newWindow.title("New Window")
 
    
    newWindow.geometry("400x400")
 
    
    Label(newWindow, 
          text ="This is a new window").pack()
def openNewWindow3():
     
    
    newWindow = Toplevel(master)
 
    
    newWindow.title("New Window")
 
    
    newWindow.geometry("400x400")
 
    
    Label(newWindow, 
          text ="This is a new window").pack()
    

label = Label(master, 
              text ="This is the main window")
 
label.pack(pady = 10)
 

btn1 = Button(master, 
             text ="Click to open a new window", 
             command = openNewWindow)
btn2 = Button(master, 
             text ="Click to open a new window", 
             command = openNewWindow2)
btn3 = Button(master, 
             text ="Click to open a new window", 
             command = openNewWindow3)
btn1.pack(pady = 10)
btn2.pack(pady = 10)
btn3.pack(pady = 10)

mainloop()