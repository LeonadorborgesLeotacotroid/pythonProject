#Este código muestra una pequeña ventana con un botón que al presionarlo te muestra un alert (ventana emergente) con un saludo

import tkinter as tk
from tkinter import messagebox


def saludar():
    messagebox.showinfo("Saludo", "¡Hola, mundo!") # Ventana emergente con el mensaje de saludo


root = tk.Tk()
boton = tk.Button(root, text="Saludar", command=saludar) #esto crea el botón mas no lo añade visualmente
boton.pack() #Esto añade el botón visualmente a la ventana

root.mainloop()