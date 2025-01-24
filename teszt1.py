from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu  
from tkinter import *
from tkinter.ttk import *

root =Tk()

root.geometry("600x600")

        
        
def openNewWindow(title):
    def convert():
        try:
            value = float(entry_value.get())  # A bevitt értéket próbáljuk float-ra alakítani
        except ValueError:
            label_result.config(text="Hiba: Kérem adjon meg egy számot!")  # Hibás input esetén üzenet
            return
        
        # Használjuk a .get() metódust a StringVar-ok értékének lekéréséhez
        from_unit_value = from_unit.get()
        to_unit_value = to_unit.get()
        
        # Átváltás a megfelelő mértékegységek között
        if from_unit_value == "méter" and to_unit_value == "centiméter":
            result = value * 100
        elif from_unit_value == "méter" and to_unit_value == "kilométer":
            result = value / 1000
        elif from_unit_value == "centiméter" and to_unit_value == "méter":
            result = value / 100
        elif from_unit_value == "centiméter" and to_unit_value == "kilométer":
            result = value / 100000
        elif from_unit_value == "kilométer" and to_unit_value == "méter":
            result = value * 1000
        elif from_unit_value == "kilométer" and to_unit_value == "centiméter":
            result = value * 100000
        else:
            result = value
        
        # Eredmény megjelenítése
        label_result.config(text="Eredmény: " + str(result))  # Itt már str() segítségével alakítjuk át
        
    newWindow = Toplevel(root)
    newWindow.title(title)
    newWindow.geometry("400x400")
    
    if title == "Hossz":
        label_value = Label(newWindow, text="Érték:")
        label_value.grid(row=0, column=0)
        entry_value = Entry(newWindow)
        entry_value.grid(row=0, column=1)

        # Kiválasztó menük az egyes mértékegységekhez
        label_from_unit = Label(newWindow, text="Forrás mértékegység:")
        label_from_unit.grid(row=1, column=0)
        from_unit = StringVar(value="méter")
        dropdown_from = OptionMenu(newWindow, from_unit, "méter", "centiméter", "kilométer")
        dropdown_from.grid(row=1, column=1)

        label_to_unit = Label(newWindow, text="Cél mértékegység:")
        label_to_unit.grid(row=2, column=0)
        to_unit = StringVar(value="centiméter")
        dropdown_to = OptionMenu(newWindow, to_unit, "méter", "centiméter", "kilométer")
        dropdown_to.grid(row=2, column=1)

        # Átváltás gomb
        button_convert = Button(newWindow, text="Átváltás", command=convert)
        button_convert.grid(row=3, column=0, columnspan=2)

        # Eredmény megjelenítése
        label_result = Label(newWindow, text="Eredmény:")
        label_result.grid(row=4, column=0, columnspan=2)
        
    label = Label(root, text="Főablak")
    label.grid(row=0, column=0, pady=10)

btn1 = Button(root, text="Tömeg átváltás", command=lambda: openNewWindow("Tömeg"))
btn2 = Button(root, text="Hossz átváltás", command=lambda: openNewWindow("Hossz"))
btn3 = Button(root, text="Idő átváltás", command=lambda: openNewWindow("Idő"))
btn1.grid(row=1, column=0, pady=10)
btn2.grid(row=2, column=0, pady=10)
btn3.grid(row=3, column=0, pady=10)

mainloop()