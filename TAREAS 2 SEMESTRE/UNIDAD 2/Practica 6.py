import tkinter as tk
import mysql.connector

class Calificaciones(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("INGRESA TU PROMEDIO")
        self.pack()
        self.crear_widgets()
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="calificacion"
        )
        self.cursor = self.db_connection.cursor()

    def crear_widgets(self):
        self.materias = ["POO", "QUIMICA", "CALCULO", "ALGEBRA", "CONTABILIDAD"]
        self.labels = []
        self.entradas = []
        for i in range(5):
            self.labels.append(tk.Label(self, text=self.materias[i]))
            self.labels[i].grid(row=i, column=0, padx=10, pady=10, sticky="W")
            self.entradas.append(tk.Entry(self))
            self.entradas[i].grid(row=i, column=1, padx=10, pady=10)

        self.calcular_button = tk.Button(self, text="CALCULAR", command=self.salvar_calificaciones)
        self.calcular_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.promedio_label = tk.Label(self, text="")
        self.promedio_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

       #aqui se centra la venta, creditos:ananotas.com
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def salvar_calificaciones(self):
        calificaciones = []
        for entry in self.entradas:
            calificacion = float(entry.get())
            calificaciones.append(calificacion)
        promedio = sum(calificaciones) / len(calificaciones)
        self.promedio_label.config(text=f"Tu promedio final es: {promedio:.2f}")

        sql = "INSERT INTO promedios (mat1, mat2, mat2, mat4, mat5, promedio) VALUES (%s, %s, %s, %s, %s, %s)"
        values = tuple(calificaciones) + (promedio,)
        self.cursor.execute(sql, values)
        self.db_connection.commit()

root = tk.Tk()
app = Calificaciones(master=root)
app.mainloop()
