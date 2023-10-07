from cProfile import label
#import tkinter as tk 

import tkinter as tk
from tkinter import messagebox
#import os
import re

def guardar_datos():
    # Obtener los datos de las entradas
    nombres = txt_nombre.get()
    apellidos = txt_apellidos.get()
    edades = txt_edad.get()
    estaturas = txt_estatura.get()
    telefonos = txt_telefono.get()

    # Obtener el género seleccionado
    genero = ""
    if var_hombre.get() == 1:
        genero = "Hombre"
    elif var_mujer.get() == 1:
        genero = "Mujer"

    #validar Que los campos tengan el formato correcto 
    if(es_entero_valido(edades) and es_decimal_valido(estaturas) and
       es_entero_valido_de_10_digitos(telefonos) and es_text_valido(nombres) and es_text_valido(apellidos)):
        #crear una cadena con los datos 
        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nTelefonos: {telefonos}\nEdades: {edades} años\nEstaturas: {estaturas} cm\nGenero: {genero}\n"
        
        #guardar los datos en un archivo de texto 
        with open("datos.text","a") as archivo:
            archivo.write(datos + "\n\n")
            
        #mostrar los datos guardados 
        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n"+datos)
        
        #limpiar datos 
        limpiar_datos()
    else:
        messagebox.showerror("Eror","Porfavor Ingrese Datos Válidos en los Campos.")

def limpiar_datos():
    txt_nombre.delete(0, "end")
    txt_apellidos.delete(0, "end")
    txt_edad.delete(0, "end")
    txt_estatura.delete(0, "end")
    txt_telefono.delete(0, "end")

def cancelar_datos():
    respuesta = messagebox.askyesno("Información", "¿Seguro que quieres cancelar los datos?")
    if respuesta:
        limpiar_datos()
        messagebox.showinfo("Información", "¡Se eliminaron los datos exitosamente!")
        
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
        
def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_text_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$",valor))
      

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos")
ventana.geometry("400x400")

# Variables para el género
var_hombre = tk.IntVar()
var_mujer = tk.IntVar()

# Crear etiquetas y entradas de texto
lbl_nombre = tk.Label(ventana, text="Nombres:")
lbl_nombre.pack()
txt_nombre = tk.Entry(ventana)
txt_nombre.pack()

lbl_apellidos = tk.Label(ventana, text="Apellidos:")
lbl_apellidos.pack()
txt_apellidos = tk.Entry(ventana)
txt_apellidos.pack()

lbl_edad = tk.Label(ventana, text="Edad:")
lbl_edad.pack()
txt_edad = tk.Entry(ventana)
txt_edad.pack()

lbl_estatura = tk.Label(ventana, text="Estatura:")
lbl_estatura.pack()
txt_estatura = tk.Entry(ventana)
txt_estatura.pack()

lbl_telefono = tk.Label(ventana, text="Teléfono:")
lbl_telefono.pack()
txt_telefono = tk.Entry(ventana)
txt_telefono.pack()

# Radiobuttons para el género
lbl_genero = tk.Label(ventana, text="Género:")
lbl_genero.pack()

rb_hombre = tk.Radiobutton(ventana, text="Hombre", variable=var_hombre, value=1)
rb_hombre.pack()

rb_mujer = tk.Radiobutton(ventana, text="Mujer", variable=var_mujer, value=1)
rb_mujer.pack()

# Botones
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.pack()

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack()

btn_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar_datos)
btn_cancelar.pack()

ventana.mainloop()
