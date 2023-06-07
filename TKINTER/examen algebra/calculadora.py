import numpy as np
from numpy.linalg import det
import tkinter as tk
from tkinter import ttk, messagebox


class Cramer:
    def __init__(self, master):
        self.master = master
        self.dark_mode = False
        master.title("Método de Cramer")
        master.geometry("500x200")

        # Etiqueta para indicar al usuario que ingrese el tamaño del sistema de ecuaciones lineales
        self.label = tk.Label(
            master, text="Tamaño del sistema de ecuaciones lineales:", font=("corbel light", 18), fg="midnight blue")
        self.label.place(x=45, y=30)

        # Entrada para que el usuario ingrese el tamaño del sistema de ecuaciones lineales
        self.entry = tk.Spinbox(
            master, from_=0, to=10, width=20, state="readonly", justify="center", readonlybackground="ghost white", cursor="hand2")
        self.entry.place(x=175, y=90)

        # Validación para asegurarse de que solo se acepten números en la entrada

        # Botón para avanzar al siguiente paso
        self.next_button = ttk.Button(
            master, text="Siguiente", command=self.next, cursor="hand2")
        self.next_button.place(x=205, y=130)
        self.mode_button = ttk.Button(
            master, text="Modo Oscuro", command=self.toggle_mode, cursor="hand2")
        self.mode_button.place(x=205, y=160)

    def toggle_mode(self):
        if self.dark_mode:
            self.master.configure(bg="white")
            self.label.configure(fg="midnight blue")
            self.mode_button.configure(text="Modo Oscuro")
            self.dark_mode = False
        else:
            self.master.configure(bg="black")
            self.label.configure(fg="white")
            self.mode_button.configure(text="Modo Claro")
            self.dark_mode = True

    def validate(self, a, b):
        if not (a.isdigit() or (a == '-' and not b)):
            return False
        if len(b) > 3:
            return False
        return True

    def destroy(self):
        self.master.destroy()

    def next(self):
        next_ven = tk.Toplevel(self.master)
        next_ven.geometry("650x300")
        next_ven.protocol("WM_DELETE_WINDOW", self.destroy)  # Agregar la función destruir a la ventana principal

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
                entry = tk.Entry(next_ven, width=5)
                entry.configure(validate='key', validatecommand=vcmd)
                entry.grid(row=i + 3, column=2 * j + 1)
                row.append(entry)
                if j < self.n:
                    label = tk.Label(next_ven, text="=")
                    label.grid(row=i + 3, column=2 * j + 2)
            self.entries.append(row)

            # Botón para resolver el sistema de ecuaciones lineales
            self.solve_button = tk.Button(
                next_ven, text="Resolver", command=self.solve)
            self.solve_button.grid(row=self.n + 4, column=0)

    def solve(self):
            # Crear la matriz de coeficientes y el vector de términos independientes a partir de las entradas del usuario
            A = np.zeros((self.n, self.n))
            b = np.zeros(self.n)
            for i in range(self.n):
                for j in range(self.n):
                    coefficient = self.entries[i][j].get()
                    if coefficient == '':
                        messagebox.showerror("Error", "Por favor ingresa los valores de los coeficientes")
                        return
                    A[i, j] = float(coefficient)
                constant = self.entries[i][-1].get()
                if constant == '':
                    messagebox.showerror("Error", "Por favor ingresa los valores de las constantes")
                    return
                b[i] = float(constant)

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



root = tk.Tk()
my_cramer = Cramer(root)
root.mainloop()

def ventana_solve():
                    ven_res = tk.Toplevel(root)
                    ven_res.title("RESOLUCION")
                    next()

