import tkinter as tk
from tkinter import messagebox
import numpy as np


def resolver():
    try:
        # Obtener el tamaño del sistema
        n = int(entry_tamano.get())

        # Crear matrices vacías para los coeficientes y los términos constantes
        A = np.zeros((n, n))
        b = np.zeros(n)

        # Llenar las matrices con los valores ingresados por el usuario
        for i in range(n):
            for j in range(n):
                A[i, j] = float(entries_coef[i][j].get())
            b[i] = float(entries_const[i].get())

        # Resolver el sistema y mostrar el resultado
        x = np.linalg.solve(A, b)
        messagebox.showinfo("Resultado", "La solución es: " + str(x))
    except:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")


def actualizar_interfaz():
    try:
        # Obtener el tamaño del sistema
        n = int(entry_tamano.get())

        # Eliminar entradas antiguas si existen
        if entries_coef:
            for fila in entries_coef:
                for entry in fila:
                    entry.destroy()
            entries_coef.clear()

        if entries_const:
            for entry in entries_const:
                entry.destroy()
            entries_const.clear()

        # Crear nuevas entradas para los coeficientes y los términos constantes
        for i in range(n):
            fila = []
            for j in range(n):
                entry = tk.Entry(ventana)
                entry.grid(row=i + 2, column=j)
                fila.append(entry)
            entries_coef.append(fila)

            entry = tk.Entry(ventana)
            entry.grid(row=i + 2, column=n)
            entries_const.append(entry)
    except:
        pass


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resolver sistema de ecuaciones lineales")

# Crear entrada para el tamaño del sistema
label_tamano = tk.Label(ventana, text="Tamaño del sistema:")
label_tamano.grid(row=0, column=0)

entry_tamano = tk.Entry(ventana)
entry_tamano.grid(row=0, column=1)

# Crear botón para actualizar la interfaz
boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_interfaz)
boton_actualizar.grid(row=1, column=0)

# Crear listas vacías para las entradas de los coeficientes y los términos constantes
entries_coef = []
entries_const = []

# Crear botón para resolver el sistema
boton_resolver = tk.Button(ventana, text="Resolver", command=resolver)
boton_resolver.grid(row=1, column=1)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
