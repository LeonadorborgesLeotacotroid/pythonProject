import numpy as np
from numpy.linalg import det
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Cramer:
    def __init__(self, master):
        try:
            next_ven.withdraw()
            result_window.withdraw()
        except Exception:
            pass

        self.master = master
        master.title("Metodo de Crammer")
        master.geometry("500x200")

        # Etiqueta para indicar al usuario que ingrese el tamaño del sistema de ecuaciones lineales
        self.label = tk.Label(
            master, text="Tamaño del sistema de ecuaciones lineales:", font=("corbel light", 18), fg="midnight blue")
        self.label.place(x=45, y=30)

        # Entrada para que el usuario ingrese el tamaño del sistema de ecuaciones lineales
        self.entry = tk.Spinbox(
            master, from_=2, to=10, width=20, state="readonly", justify="center", readonlybackground="ghost white", cursor="hand2")
        self.entry.place(x=175, y=90)

        # Validación para asegurarse de que solo se acepten números en la entrada

        # Botón para avanzar al siguiente paso
        self.next_button = ttk.Button(
            master, text="Siguiente", command=self.next, cursor="hand2")
        self.next_button.place(x=205, y=130)
        master.resizable(0, 0)

    def validate(self, a, b):

        if len(b) > 3:
            return False

        return a.isdigit()

    def des1(self):
        try:
            root.deiconify()
            next_ven.withdraw()
        except Exception:
            pass

    def des2(self):
        try:
            next_ven.deiconify()
            result_window.withdraw()
        except Exception:
            pass

    def next(self):
        try:
            root.withdraw()
            result_window.withdraw()
        except Exception:
            pass

        global next_ven

        next_ven = tk.Toplevel(self.master)
        next_ven.title("Ingrese los datos en las casillas")
        # Obtener el tamaño del sistema de ecuaciones lineales ingresado por el usuario SE GENERA LA NUEVA VENTANA
        self.n = int(self.entry.get())

        # Ocultar la entrada y el botón de siguiente
        self.entry.grid_forget()
        self.next_button.grid_forget()

        vcmd = (self.master.register(self.validate), '%S', '%P')

        # Crear entradas para que el usuario ingrese los coeficientes y términos independientes del sistema de ecuaciones lineales
        self.entries = []
        for i in range(self.n):
            row = []
            for j in range(self.n + 1):
                if j < self.n:
                    label = tk.Label(next_ven, text=f"x{j + 1}")
                    label.grid(row=i + 3, column=2 * j)
                entry = tk.Entry(next_ven, width=6, justify="center", bd=0)
                entry.configure(validate='key', validatecommand=vcmd)
                entry.grid(row=i + 3, column=2 * j+1)
                row.append(entry)
                if j < self.n:
                    label = tk.Label(next_ven, text="=")
                    label.grid(row=i + 3, column=2*j+2)
            self.entries.append(row)

        # Botón para resolver el sistema de ecuaciones lineales
        self.solve_button = ttk.Button(
            next_ven, text="Resolver", command=self.solve)
        self.solve_button.grid(row=self.n*5, column=j)
        next_ven.resizable(0, 0)
        next_ven.protocol("WM_DELETE_WINDOW", self.des1)

    def solve(self):

        global result_window

        try:
            next_ven.withdraw()
            root.withdraw()
        except Exception:
            pass

        # Crear la matriz de coeficientes y el vector de términos independientes a partir de las entradas del usuario
        # Crear la matriz de coeficientes y el vector de términos independientes a partir de las entradas del usuario
        A = np.zeros((self.n, self.n))
        b = np.zeros(self.n)

        for i in range(self.n):
            for j in range(self.n):
                coefficient = self.entries[i][j].get()
                if coefficient == '':
                    messagebox.showinfo(
                        "Error", "Por favor ingresa los valores de los coeficientes")
                    return next_ven.deiconify()
                A[i, j] = float(coefficient)
            constant = self.entries[i][-1].get()
            if constant == '':
                messagebox.showinfo(
                    "Error", "Por favor ingresa los valores de las constantes")
                return next_ven.deiconify()

        for i in range(self.n):
            for j in range(self.n):
                A[i, j] = float(self.entries[i][j].get())
            b[i] = float(self.entries[i][-1].get())

        # Aplicar el método de Cramer para resolver el sistema de ecuaciones lineales
        detA = det(A)

        # Si el determinante de la matriz de coeficientes es cero, el sistema no tiene solución única
        if detA == 0:
            result_window = tk.Toplevel(self.master)
            result_label = tk.Label(
                result_window, text="El sistema no tiene solución única")
            result_label.pack()
            return

        x = np.zeros(self.n)

        step_descriptions = []

        for i in range(self.n):
            Ai = A.copy()
            Ai[:, i] = b
            x[i] = det(Ai) / detA

            # Agregar una descripción detallada del paso realizado para calcular cada solución
            step_descriptions.append(
                f"Reemplazar la columna {i + 1} por el vector b: \n{Ai}\nCalcular el determinante: {det(Ai)}\nDividir por el determinante de A: {det(Ai)}/{detA}={x[i]}")

        # Mostrar una ventana con las respuestas y el procedimiento paso a paso
        result_window = tk.Toplevel(self.master)

        result_label = tk.Label(result_window, text=f"Respuestas: {x}")
        result_label.pack()

        for description in step_descriptions:
            step_label = tk.Label(result_window, text=f"{description}")
            step_label.pack()

        check_label = tk.Label(
            result_window, text=f"Comprobación: {np.allclose(A @ x, b)}")
        check_label.pack()
        result_window.protocol("WM_DELETE_WINDOW", self.des2)


root = tk.Tk()
my_cramer = Cramer(root)
root.mainloop()


def ventana_solve():
    ven_res = tk.Toplevel(root)
    ven_res.title("RESOLUCION")
    next()