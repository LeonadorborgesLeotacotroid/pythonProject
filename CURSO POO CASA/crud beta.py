import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime

class TareasApp:
    def __init__(self, master):
        self.master = master
        master.title("Tareas App")

        # Conexión a la base de datos
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="p"
        )
        self.cursor = self.conn.cursor()

        # Crear tabla si no existe
        self.crear_tabla()

        # Etiquetas
        self.id_label = tk.Label(master, text="ID:")
        self.asignatura_label = tk.Label(master, text="Asignatura:")
        self.valor_label = tk.Label(master, text="Valor de la tarea:")
        self.fecha_label = tk.Label(master, text="Fecha de entrega:")
        self.descripcion_label = tk.Label(master, text="Descripción:")

        # Entradas
        vcmd_id = (master.register(self.validate_id), '%P')
        self.id_entry = tk.Entry(master, validate='key', validatecommand=vcmd_id)

        self.asignatura_entry = ttk.Combobox(master, values=["Asignatura 1", "Asignatura 2", "Asignatura 3"],state="readonly")

        vcmd_valor = (master.register(self.validate_valor), '%P')
        self.valor_entry = tk.Entry(master, validate='key', validatecommand=vcmd_valor)

        self.fecha_entry = DateEntry(master,state="readonly")

        self.descripcion_entry = tk.Entry(master)

        # Botones
        self.guardar_button = tk.Button(master, text="Guardar", command=self.guardar)
        self.actualizar_button = tk.Button(master, text="Actualizar", command=self.actualizar)
        self.eliminar_button = tk.Button(master, text="Eliminar", command=self.eliminar)
        self.buscar_button = tk.Button(master, text="Buscar", command=self.buscar)
        self.cancelar_busqueda_button = tk.Button(master, text="Cancelar búsqueda", command=self.mostrar_datos)

        # Tabla
        columns = ("#1", "#2", "#3", "#4", "#5")
        self.tabla = ttk.Treeview(master, columns=columns, show="headings")
        self.tabla.heading("#1", text="ID")
        self.tabla.heading("#2", text="Asignatura")
        self.tabla.heading("#3", text="Valor")
        self.tabla.heading("#4", text="Fecha")
        self.tabla.heading("#5", text="Descripción")

        # Mostrar datos en la tabla
        self.mostrar_datos()

        # Posicionar elementos en la ventana
        self.id_label.grid(row=0, column=0)
        self.id_entry.grid(row=0, column=1)

        self.asignatura_label.grid(row=1, column=0)
        self.asignatura_entry.grid(row=1, column=1)

        self.valor_label.grid(row=2, column=0)
        self.valor_entry.grid(row=2, column=1)

        self.fecha_label.grid(row=3, column=0)
        self.fecha_entry.grid(row=3, column=1)

        self.descripcion_label.grid(row=4, column=0)
        self.descripcion_entry.grid(row=4, column=1)

        self.guardar_button.grid(row=5, column=0)
        self.actualizar_button.grid(row=5, column=1)
        self.eliminar_button.grid(row=5, column=2)
        self.buscar_button.grid(row=6, column=0)
        self.cancelar_busqueda_button.grid(row=6, column=1)

        self.tabla.grid(row=7, column=0, columnspan=3)

    def validate_id(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) >= 0 and int(new_text) < 1000:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_valor(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) < 1000:
                return True
            else:
                return False
        except ValueError:
            return False
    def validar_descripcion(self, new_text):
        if not new_text:
            return True
        try:
            if str(new_text) > 0 and str(new_text) < 25:
                return True
            else:
                return False
        except ValueError:
            return False

    def crear_tabla(self):
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS tareas (
                   id INT PRIMARY KEY,
                   asignatura VARCHAR(255),
                   valor INT,
                   fecha DATE,
                   descripcion TEXT
               )
           """)
        self.conn.commit()

    def guardar(self):
        id = self.id_entry.get()
        asignatura = self.asignatura_entry.get()
        valor = self.valor_entry.get()
        fechastr = self.fecha_entry.get()
        fecha = datetime.strptime(fechastr, '%m/%d/%y')
        descripcion = self.descripcion_entry.get()

        if not id or not asignatura or not valor or not fecha or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            self.cursor.execute("""
                   INSERT INTO tareas (id, asignatura, valor, fecha, descripcion)
                   VALUES (%s, %s, %s, %s, %s)
               """, (id, asignatura, valor, fecha, descripcion))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Tarea guardada con éxito")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "Ya existe una tarea con ese ID")

    def actualizar(self):
        id = self.id_entry.get()
        asignatura = self.asignatura_entry.get()
        valor = self.valor_entry.get()
        fechastr = self.fecha_entry.get()
        fecha = datetime.strptime(fechastr, '%m/%d/%y')
        descripcion = self.descripcion_entry.get()

        if not id or not asignatura or not valor or not fecha or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            self.cursor.execute("""
                   UPDATE tareas SET asignatura=%s, valor=%s, fecha=%s, descripcion=%s WHERE id=%s
               """, (asignatura, valor, fecha, descripcion, id))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Tarea actualizada con éxito")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "No existe una tarea con ese ID")

    def eliminar(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showerror("Error", "El campo ID es obligatorio")
            return

        try:
            self.cursor.execute("""
                   DELETE FROM tareas WHERE id=%s
               """, (id,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Tarea eliminada con éxito")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "No existe una tarea con ese ID")

    def buscar(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showerror("Error", "El campo ID es obligatorio")
            return

        # Limpiar tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener datos de la base de datos
        self.cursor.execute("SELECT id, asignatura, valor, fecha, descripcion FROM tareas WHERE id=%s", (id,))
        row = self.cursor.fetchone()

        if row:
            # Mostrar datos en la tabla
            self.tabla.insert("", tk.END, values=row)
        else:
            messagebox.showerror("Error", "No existe una tarea con ese ID")

    def mostrar_datos(self):
        # Limpiar tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener datos de la base de datos
        self.cursor.execute("SELECT id, asignatura, valor, fecha, descripcion FROM tareas ORDER BY fecha ASC")
        rows = self.cursor.fetchall()

        # Mostrar datos en la tabla
        for row in rows:
            self.tabla.insert("", tk.END, values=row)

    def limpiar_entradas(self):
        self.id_entry.delete(0, tk.END)
        self.asignatura_entry.set('')
        self.valor_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
        root = tk.Tk()
        app = TareasApp(root)
        root.mainloop()
