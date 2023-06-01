import numpy as np
from numpy.linalg import det
import tkinter as tk

class Cramer:
    def __init__(self, master):
        self.master = master
        master.title("Método de Cramer")

        # Etiqueta para indicar al usuario que ingrese el tamaño del sistema de ecuaciones lineales
        self.label = tk.Label(master, text="Tamaño del sistema de ecuaciones lineales:")
        self.label.grid(row=0, column=0)

        # Entrada para que el usuario ingrese el tamaño del sistema de ecuaciones lineales
        self.entry = tk.Entry(master)
        self.entry.grid(row=1, column=0)

        # Validación para asegurarse de que solo se acepten números en la entrada
        vcmd = (master.register(self.validate), '%P')
        self.entry.configure(validate='key', validatecommand=vcmd)

        # Botón para avanzar al siguiente paso
        self.next_button = tk.Button(master, text="Siguiente", command=self.next)
        self.next_button.grid(row=2, column=0)

    def validate(self, new_text):
        if not new_text:
            return True
        try:
            int(new_text)
            return True
        except ValueError:
            return False

    def next(self):
        # Obtener el tamaño del sistema de ecuaciones lineales ingresado por el usuario SE GENERA LA NUEVA VENTANA
        self.n = int(self.entry.get())

        # Ocultar la entrada y el botón de siguiente
        self.entry.grid_forget()
        self.next_button.grid_forget()

        vcmd = (self.master.register(self.validate), '%P')

        # Crear entradas para que el usuario ingrese los coeficientes y términos independientes del sistema de ecuaciones lineales
        self.entries = []
        for i in range(self.n):
            row = []
            for j in range(self.n + 1):
                if j < self.n:
                    label = tk.Label(self.master, text=f"x{j + 1}")
                    label.grid(row=i + 3, column=2 * j)
                entry = tk.Entry(self.master)
                entry.configure(validate='key', validatecommand=vcmd)
                entry.grid(row=i + 3, column=2 * j + 1)
                row.append(entry)
            self.entries.append(row)

        # Botón para resolver el sistema de ecuaciones lineales
        self.solve_button = tk.Button(self.master, text="Resolver", command=self.solve)
        self.solve_button.grid(row=self.n + 4, column=0)

    def solve(self):
        # Crear la matriz de coeficientes y el vector de términos independientes a partir de las entradas del usuario
        A = np.zeros((self.n, self.n))
        b = np.zeros(self.n)
        for i in range(self.n):
            for j in range(self.n):
                A[i, j] = float(self.entries[i][j].get())
            b[i] = float(self.entries[i][-1].get())

        # Aplicar el método de Cramer para resolver el sistema de ecuaciones lineales
        detA = det(A)

        # Si el determinante de la matriz de coeficientes es cero, el sistema no tiene solución única
        if detA == 0:
            result_window = tk.Toplevel(self.master)
            result_label = tk.Label(result_window, text="El sistema no tiene solución única")
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

        check_label = tk.Label(result_window, text=f"Comprobación: {np.allclose(A @ x, b)}")
        check_label.pack()


root = tk.Tk()
my_cramer = Cramer(root)
root.mainloop()
