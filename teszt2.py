import tkinter as tk
from tkinter import ttk

# Átváltási faktorok (példák)
length_units = ['yard','mérföld','kilométer','méter']
length_factors = {
    'yard': 1,
    'mérföld': 0.000568182,
    'kilométer': 0.0009144,
    'méter': 0.9144}

weight_units = ['font','kilogramm','gramm']
weight_factors = {
    'font': 1,
    'kilogramm': 0.453592,
    'gramm': 453.592}

time_units = ['másodperc','perc','óra']
time_factors = {
    'másodperc': 1,
    'perc': 60, 
    'óra': 3600 }

# Átváltás funkciók
def convert_length():
    try:
        value = float(entry.get().strip())  # Számra konvertálás
        from_unit = from_unit_combobox.get()
        result = {}
        
        # Átváltás a kiválasztott mértékegységre
        for unit in length_units:
            if unit != from_unit:
                # Az átváltási tényezőt az adott mértékegység alapján számoljuk
                factor_from = length_factors[from_unit]
                factor_to = length_factors[unit]
                converted_value = value * (factor_to / factor_from)
                result[unit] = converted_value
        
        # Eredmények kiírása
        result_label.config(text="\n".join([f"{unit}: {result[unit]:.4f}" for unit in result]))
    except ValueError:
        result_label.config(text="Érvénytelen adat! Kérem adjon meg egy számot!")

def convert_weight():
    try:
        value = float(entry.get().strip())
        from_unit = from_unit_combobox.get()
        result = {}
        
        # Átváltás a kiválasztott mértékegységre
        for unit in weight_units:
            if unit != from_unit:
                # Az átváltási tényezőt az adott mértékegység alapján számoljuk
                factor_from = weight_factors[from_unit]
                factor_to = weight_factors[unit]
                converted_value = value * (factor_to / factor_from)
                result[unit] = converted_value
        
        # Eredmények kiírása
        result_label.config(text="\n".join([f"{unit}: {result[unit]:.4f}" for unit in result]))
    except ValueError:
        result_label.config(text="Érvénytelen adat! Kérem adjon meg egy számot!")

def convert_time():
    try:
        value = float(entry.get().strip())
        from_unit = from_unit_combobox.get()
        result = {}
        
        # Az idő mértékegységei: second, minute, hour
        if from_unit == 'másodperc':
            # Másodperc átváltása percre és órára
            percek = value / 60
            orak = value / 3600
            result = {
                'perc': percek,
                'óra': orak
            }
        
        elif from_unit == 'perc':
            # Perc átváltása másodpercre és órára
            masodpercek = value * 60
            orak = value / 60
            result = {
                'second': masodpercek,
                'hour': orak
            }
        
        elif from_unit == 'óra':
            # Óra átváltása percre és másodpercre
            masodpercek = value * 3600
            percek = value * 60
            result = {
                'másodperc': masodpercek,
                'perc': percek
            }
        
        # Eredmények kiírása
        result_label.config(text="\n".join([f"{unit.capitalize()}: {result[unit]:.4f}" for unit in result]))
        
    except ValueError:
        result_label.config(text="Érvénytelen adat! Kérem adjon meg egy számot!")

# Főablak
root = tk.Tk()
root.title("Mértékegység Átváltó")

# Cím
title_label = tk.Label(root, text="Mértékegység Átváltó", font=("Arial", 20))
title_label.pack(pady=20)

# Gombok a mértékegységek típusához
def open_length_conversion():
    conversion_window('hossz', length_units, length_factors)

def open_weight_conversion():
    conversion_window('tömeg', weight_units, weight_factors)

def open_time_conversion():
    conversion_window('idő', time_units, time_factors)

# Közös konverziós ablak
def conversion_window(type_name, units, factors):
    # Új ablak nyitása
    conversion_window = tk.Toplevel(root)
    conversion_window.title(f"{type_name.capitalize()} Átváltás")
    
    # Beviteli mező
    tk.Label(conversion_window, text="Érték:").pack(pady=5)
    global entry
    entry = tk.Entry(conversion_window)
    entry.pack(pady=5)

    # Legördülő lista a kezdő mértékegységhez
    tk.Label(conversion_window, text="Kezdő mértékegység:").pack(pady=5)
    global from_unit_combobox
    from_unit_combobox = ttk.Combobox(conversion_window, values=units)
    from_unit_combobox.set(units[0])  # Alapértelmezett érték
    from_unit_combobox.pack(pady=5)

    # Gomb a számoláshoz
    if type_name == 'hossz':
        convert_button = tk.Button(conversion_window, text="Számolás", command=convert_length)
    elif type_name == 'tömeg':
        convert_button = tk.Button(conversion_window, text="Számolás", command=convert_weight)
    else:
        convert_button = tk.Button(conversion_window, text="Számolás", command=convert_time)
    
    convert_button.pack(pady=5)

    # Eredmények label
    global result_label
    result_label = tk.Label(conversion_window, text="")
    result_label.pack(pady=5)

    # Bezárás gomb
    close_button = tk.Button(conversion_window, text="Bezárás", command=conversion_window.destroy)
    close_button.pack(pady=5)

# Gombok a főablakban
length_button = tk.Button(root, text="Hossz Átváltás", command=open_length_conversion)
length_button.pack(pady=10)

weight_button = tk.Button(root, text="Tömeg Átváltás", command=open_weight_conversion)
weight_button.pack(pady=10)

time_button = tk.Button(root, text="Idő Átváltás", command=open_time_conversion)
time_button.pack(pady=10)

# Kilépés gomb
exit_button = tk.Button(root, text="Kilépés", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
