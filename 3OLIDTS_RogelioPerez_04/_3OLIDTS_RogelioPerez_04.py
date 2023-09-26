from cProfile import label
import tkinter as tk 

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label1 = tk.Label(ventana, text = 'Frenheit')
label1.grid(row = 0, column = 0)

entry1 = tk.Entry(ventana)
entry1.grid(row = 0, column = 1)

button1 = tk.Button(ventana, text="Convertir a Celcius")
button1.grid(row = 0, column=2)

label2 = tk.Label(ventana, text='Celsius')
label2.grid(row = 1, column=0)

entry2 = tk.Entry(ventana)
entry2.grid(row = 1, column = 0)

button2 = tk.Button(ventana, text = "Convertir a Farenheit")
button2.grid(row = 1, column = button2)

button3 = tk.Button(ventana, text = "Restablecer")
button3.grid(row = 2, column =  )
             

