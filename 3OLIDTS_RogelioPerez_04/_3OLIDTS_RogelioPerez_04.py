from cProfile import label
#import tkinter as tk 

import tkinter as tk

def borrar():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")


def convertir_a_farenheit():
    Celsius = float(entry2.get())
    Farenheit = (Celsius * 9 / 5) + 32
    entry1.delete(0, tk.END)
    entry1.insert(0,f"{Farenheit:.2f}")

def convertir_a_celsius():
    Fahrenheit = float(entry1.get())
    Celsius = (Fahrenheit-32)*5.0/9.0
    entry2.delete(0, tk.END)
    entry2.insert(0,f"{Celsius:.2f}")


ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label1 = tk.Label(ventana, text = 'Frenheit')
label1.grid(row = 0, column = 0)

entry1 = tk.Entry(ventana)
entry1.grid(row = 0, column = 1)

button1 = tk.Button(ventana, text="Convertir a Celcius", command = convertir_a_celsius)
button1.grid(row = 0, column=2)

label2 = tk.Label(ventana, text='Celsius')
label2.grid(row = 1, column=0)

entry2 = tk.Entry(ventana)
entry2.grid(row = 1, column = 1)

button2 = tk.Button(ventana, text = "Convertir a Farenheit", command = convertir_a_farenheit)
button2.grid(row = 1, column = 2)

button3 = tk.Button(ventana, text = "Restablecer", command = borrar)
button3.grid(row = 2, column = 1 )

ventana.geometry("520x480")

ventana.mainloop()
             

