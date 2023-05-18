from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import sys
from subprocess import call
from datetime import datetime

class TareasApp:
    def __init__(self, master):
        self.master = master
        master.title("TAREAS")
        self.master.config(bd=10, bg="azure")
        self.master.geometry("1080x750")
        self.master.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico")

        self.titulo = Label(master, text="ANOTA TUS TAREAS", fg="black", bg="azure", font=("Arial", 20, "bold"),pady=10).grid()

        marco = LabelFrame(master, text="DATOS DE LA TAREA", bg="azure", font=("Arial", 15, "bold"), pady=5)
        marco.config(bd=2, bg="azure")
        marco.grid()

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
        self.id_label = tk.Label(marco,text="ID:", bg="azure", font=("Ariual", 12, "bold"))
        self.asignatura_label = tk.Label(marco, text="ASÍGNATURA:", bg="azure", font=("Ariual", 12, "bold"))
        self.valor_label = tk.Label(marco, text="VALOR DE LA TAREA:", bg="azure", font=("Ariual", 12, "bold"))
        self.fecha_label = tk.Label(marco, text="FECHA DE ENTREGA:", bg="azure", font=("Ariual", 12, "bold"))
        self.descripcion_label = tk.Label(marco, text="DESCRIPCIÓN:", bg="azure", font=("Ariual", 12, "bold"))

        # Entradas
        vcmd_id = (marco.register(self.validate_id), '%P')
        self.id_entry = tk.Entry(marco, validate='key', validatecommand=vcmd_id, width=25, font=("Arial", 12, "bold"))

        self.asignatura_entry = ttk.Combobox(marco, values=["PROGRAMACIÓN", "CÁLCULO", "QUÍMICA", "ALGEBRA", "INGLES", "TUTORÍAS", "PROBABILIDAD"],width=22,font=("Arial", 12, "bold"),state="readonly")

        vcmd_valor = (marco.register(self.validate_valor), '%P')
        self.valor_entry = tk.Entry(marco, validate='key', validatecommand=vcmd_valor, width=25, font=("Arial", 12, "bold"))

        self.fecha_entry = DateEntry(marco,state="readonly", width=15, font=("Arial", 12, "bold"))

        vcmd_descricpcion = (marco.register(self.validate_descripcion), '%P')
        self.descripcion_entry = tk.Entry(marco,validate="key",validatecommand=vcmd_descricpcion, width=25, font=("Arial", 12, "bold"))

        marcobot = LabelFrame(master, bg="azure", pady="10")
        marcobot.config(bd=0, bg="azure")
        marcobot.grid(padx=120)
        # Botones
        self.guardar_button = tk.Button(marcobot, text="GUARDAR", command=self.guardar, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold"))
        self.actualizar_button = tk.Button(marcobot, text="ACTUALIZAR", command=self.actualizar, height=2, width=12,bg="springgreen4", fg="white", font=("Arial", 12, "bold"))
        self.eliminar_button = tk.Button(marcobot, text="ELIMINAR", command=self.eliminar,height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold") )
        self.buscar_button = tk.Button(marcobot, text="BUSCAR", command=self.buscar, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold"))
        self.cancelar_busqueda_button = tk.Button(marcobot, text="CANCELAR BÚSQUEDA", command=self.mostrar_datos, height=2, width=20,bg="springgreen4", fg="white", font=("Arial", 12, "bold"))

        # Tabla
        columns = ("#1", "#2", "#3", "#4", "#5")
        self.tabla = ttk.Treeview(master, columns=columns, show="headings")
        self.tabla.heading("#1", text="ID")
        self.tabla.heading("#2", text="ASIGNATURA")
        self.tabla.heading("#3", text="VALOR")
        self.tabla.heading("#4", text="FECHA")
        self.tabla.heading("#5", text="DESCRIPCIÓN")

        # Mostrar datos en la tabla
        self.mostrar_datos()

        # Posicionar elementos en la ventana
        self.id_label.grid(row=0, column=0, padx=25,pady=10)
        self.id_entry.grid(row=0, column=1, padx=25,pady=10)

        self.asignatura_label.grid(row=1, column=0, padx=25,pady=10)
        self.asignatura_entry.grid(row=1, column=1, padx=25,pady=10)

        self.valor_label.grid(row=2, column=0, padx=25,pady=10)
        self.valor_entry.grid(row=2, column=1, padx=25,pady=10)

        self.fecha_label.grid(row=3, column=0, padx=25,pady=10)
        self.fecha_entry.grid(row=3, column=1, padx=25,pady=10)

        self.descripcion_label.grid(row=4, column=0, padx=25,pady=10)
        self.descripcion_entry.grid(row=4, column=1, padx=25,pady=10)

        self.guardar_button.grid(row=0, column=0, padx=15, pady=5)
        self.actualizar_button.grid(row=0, column=1,padx=15, pady=5)
        self.eliminar_button.grid(row=0, column=2, padx=15, pady=5)
        self.buscar_button.grid(row=0, column=3,padx=15, pady=10)
        self.cancelar_busqueda_button.grid(row=0, padx=15, column=4, pady=10)

        self.tabla.grid()

        marcofal = LabelFrame(master, bg="azure", pady="10")
        marcofal.config(bd=0, bg="azure")
        marcofal.grid(padx=120)

        self.guardar_button = tk.Button(marcofal, text="REGRESAR", command=self.back, height=2, width=12,
                                        bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0,padx=15, pady=10)
        self.actualizar_button = tk.Button(marcofal, text="SALIR", command=self.log, height=2, width=10,
                                           bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1,padx=15, pady=10)

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

    def validate_descripcion(self, new_text):
        if not new_text:
            return True
        if len(new_text) <= 20:
            return True
        else:
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

    def crear_tabla(self):
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS tareas (
                   id INT PRIMARY KEY,
                   asignatura VARCHAR(20),
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
            messagebox.showerror("ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS")
            return

        try:
            self.cursor.execute("""
                   INSERT INTO tareas (id, asignatura, valor, fecha, descripcion)
                   VALUES (%s, %s, %s, %s, %s)
               """, (id, asignatura, valor, fecha, descripcion))
            self.conn.commit()
            messagebox.showinfo("ÉXITO", "TAREA GUARDADA CON ÉXITO")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("ERROR", "YA EXISTE UNA TAREA CON ESE ID")

    def actualizar(self):
        id = self.id_entry.get()
        asignatura = self.asignatura_entry.get()
        valor = self.valor_entry.get()
        fechastr = self.fecha_entry.get()
        fecha = datetime.strptime(fechastr, '%m/%d/%y')
        descripcion = self.descripcion_entry.get()

        if not id or not asignatura or not valor or not fecha or not descripcion:
            messagebox.showerror("ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS")
            return

        try:
            self.cursor.execute("""
                   UPDATE tareas SET asignatura=%s, valor=%s, fecha=%s, descripcion=%s WHERE id=%s
               """, (asignatura, valor, fecha, descripcion, id))
            self.conn.commit()
            messagebox.showinfo("ÉXITO", "TAREA ACTUALIZADA CON ÉXITO")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("ERROR", "NO EXISTE UNA TAREA CON ESE ID")

    def eliminar(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showerror("ERROR", "EL CAMPO ID ES OBLIGATORIO")
            return

        try:
            self.cursor.execute("""
                   DELETE FROM tareas WHERE id=%s
               """, (id,))
            self.conn.commit()
            messagebox.showinfo("ÉXITO", "TAREA ELIMINADA CON ÉXITO")
            self.limpiar_entradas()
            self.mostrar_datos()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("ERROR", "NO EXISTE UNA TAREA CON ESE ID")

    def buscar(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showerror("ERROR", "EL CAMPO ID ES OBLIGATORIO")
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
            messagebox.showerror("ERROR", "NO EXISTE TAREA CON ESE ID")

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

    def back(self):
        self.master.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/MENU DESPEGABLE.py'])

    def log(self):
        self.master.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])

if __name__ == "__main__":
        root = tk.Tk()
        app = TareasApp(root)
        root.mainloop()
