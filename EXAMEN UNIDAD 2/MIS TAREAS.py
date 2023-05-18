import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Tareas:
    def __init__(self, ventana_tarea):
        self.window = ventana_tarea
        self.window.title("MIS TAREAS")
        self.window.geometry("900x670")
        self.window.resizable(0, 0)
        self.window.config(bd=10, bg="azure")
        self.window.iconbitmap(r"c:/pythonProject/EXAMEN UNIDAD 2/icono.ico")

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )

        self.cursor = self.db.cursor()

        # Create the tasks table if it doesn't already exist
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        asignatura VARCHAR(255) NOT NULL,
                        fecha_entrega DATE NOT NULL,
                        valor_tarea INT NOT NULL,
                        descripcion TEXT NOT NULL
                    )
                """)

        titulo = Label(ventana_tarea, text="ANOTA TUS TAREAS", fg="black", bg="azure", font=("Arial", 20, "bold"),
                       pady=10).pack()

        marco = LabelFrame(ventana_tarea, text="DATOS DE LA TAREA", bg="azure", font=("Arial", 15, "bold"), pady=5)
        marco.config(bd=2, bg="azure")
        marco.pack()

        label_asignatura = Label(marco, text="ASIGNATURA: ", bg="azure", font=("Ariual", 12, "bold")).grid(row=0,
                                                                                                           column=0,
                                                                                                           sticky='s',
                                                                                                           padx=5,
                                                                                                           pady=9)
        self.combo_asignatura = ttk.Combobox(marco,
                                             values=["POO", "CÁLCULO", "ÁLGEBRA", "CONTABILIDAD", "PROBABILIDAD",
                                                     "QUÍMICA"], width=22, font=("Arial", 12, "bold"), state="readonly")
        self.combo_asignatura.current(0)
        self.combo_asignatura.focus()
        self.combo_asignatura.grid(row=0, column=1, padx=5, pady=0)

        label_fecha = Label(marco, text="FECHA DE ENTREGA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=1,
                                                                                                           column=0,
                                                                                                           sticky='s',
                                                                                                           padx=5,
                                                                                                           pady=8)
        self.fecha = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.fecha.grid(row=1, column=1, padx=5, pady=8)



        label_puntaje = Label(marco, text="VALOR DE LA TAREA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky='s',
                                                                                                              padx=5,
                                                                                                              pady=8)
        self.puntaje = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.puntaje.grid(row=2, column=1, padx=5, pady=8)

        label_descripcion = Label(marco, text="DESCRIPCIÓN: ", bg="azure", font=("Arial", 12, "bold")).grid(row=3,
                                                                                                             column=0,
                                                                                                             sticky='s',
                                                                                                             padx=5,
                                                                                                             pady=8)
        self.descripcion = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.descripcion.grid(row=3, column=1, padx=5, pady=8)

        frame_botones = Frame(ventana_tarea)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        boton_registrar = Button(frame_botones, text="AÑADIR", command=self.add_task, height=2, width=10,
                                 bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1,
                                                                                                padx=10, pady=15)
        boton_eliminar = Button(frame_botones, text="ELIMINAR", command=self.delete_task, height=2, width=10,
                                bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2,
                                                                                                padx=10, pady=15)

        boton_actualizar = Button(frame_botones, text="ACTUALIZAR", command=self.update_task, height=2, width=10,
                                  bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=5,
                                                                                                  padx=10, pady=15)

        "--------------- Tabla --------------------"
        self.tree = ttk.Treeview(height=15, columns=("columna1", "columna2", "columna3"))
        self.tree.heading("#0", text="ASIGNATURA", anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)

        self.tree.heading("columna1", text='FECHA DE ENTREGA', anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna2", text='VALOR DE LA TAREA', anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna3", text='DESCRIPCIÓN', anchor=CENTER)
        self.tree.column("columna3", width=150, minwidth=75, stretch=NO)

        self.tree.pack()
        # Agregar un evento de selección a la tabla
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        self.view_tasks()

        # Mostrar las tareas en la tabla


    def on_select(self, event):
        # Obtener el elemento seleccionado
        selected_item = self.tree.selection()[0]
        # Obtener los valores del elemento seleccionado
        values = self.tree.item(selected_item)['values']
        # Asignar los valores a los campos de entrada para su edición
        self.combo_asignatura.set(values[1])
        self.fecha.insert(0, values[2])
        self.puntaje.insert(0, values[3])
        self.descripcion.delete(0, END)
        self.descripcion.insert(0, values[4])

    def add_task(self):
        # Obtener los valores de los campos de entrada
        asignatura = self.combo_asignatura.get()
        fecha = self.fecha.get()
        puntaje = self.puntaje.get()
        descripcion = self.descripcion.get()

        # Validar que los campos no estén vacíos
        if asignatura and fecha and puntaje and descripcion:
            # Insertar la tarea en la base de datos
            query = "INSERT INTO tasks (asignatura, fecha_entrega, valor_tarea, descripcion) VALUES (%s,%s,%s,%s)"
            values = (asignatura, fecha, puntaje, descripcion)
            orden= ("SELECT * FROM tasks ORDER BY fecha_entrega ASC")
            self.cursor.execute(query, values, orden)
            self.db.commit()

            # Limpiar los campos de entrada
            self.combo_asignatura.current(0)
            self.fecha.delete(0, END)
            self.puntaje.delete(0, END)
            self.descripcion.delete(0, END)

            # Actualizar la tabla
            self.view_tasks()
        else:
            # Mostrar un mensaje de error si algún campo está vacío
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def delete_task(self):
        # Obtener el elemento seleccionado en la tabla
        selected_item = self.tree.selection()[0]
        # Obtener el ID del elemento seleccionado
        task_id = self.tree.item(selected_item)['values'][0]

        # Eliminar la tarea de la base de datos
        query = "DELETE FROM tasks WHERE id = %s"
        self.cursor.execute(query, (task_id,))
        self.db.commit()

        # Actualizar la tabla
        self.view_tasks()

    def update_task(self):
        # Obtener el elemento seleccionado en la tabla
        selected_item = self.tree.selection()[0]
        # Obtener el ID del elemento seleccionado
        task_id = self.tree.item(selected_item)['values'][0]

        # Obtener los valores de los campos de entrada
        asignatura = self.combo_asignatura.get()
        fecha = self.fecha.get()
        puntaje = self.puntaje.get()
        descripcion = self.descripcion.get()

        # Validar que los campos no estén vacíos
        if asignatura and fecha and puntaje and descripcion:
            # Actualizar la tarea en la base de datos
            query = "UPDATE tasks SET asignatura = %s, fecha_entrega = %s, valor_tarea = %s, descripcion = %s WHERE id = %s"
            values = (asignatura, fecha, puntaje, descripcion, task_id)
            self.cursor.execute(query, values)
            self.db.commit()

            # Limpiar los campos de entrada
            self.combo_asignatura.current(0)
            self.fecha.delete(0, END)
            self.puntaje.delete(0, END)
            self.descripcion.delete(0, END)

            # Actualizar la tabla
            self.view_tasks()
        else:
            # Mostrar un mensaje de error si algún campo está vacío
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def view_tasks(self):
        # Eliminar todos los elementos de la tabla
        self.tree.delete(*self.tree.get_children())

        # Obtener todas las tareas de la base de datos
        query = "SELECT * FROM tasks ORDER BY asignatura"
        self.cursor.execute(query)
        tasks = self.cursor.fetchall()

        # Agregar las tareas a la tabla
        for task in tasks:
            self.tree.insert('', END, values=task)


if __name__ == "__main__":
    # Crear una ventana de aplicación
    window = Tk()
    # Crear una instancia de la clase Tareas
    app = Tareas(window)
    # Ejecutar el bucle principal de la aplicación
    window.mainloop()