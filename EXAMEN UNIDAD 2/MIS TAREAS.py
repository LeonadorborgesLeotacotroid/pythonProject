import sys
from subprocess import call
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call

import sqlite3

class Tareas:
    db_name = 'database_proyecto.db'

    def __init__(self, ventana_tarea):
        self.window = ventana_tarea
        self.window.title("MIS TAREAS")
        self.window.geometry("900x670")
        self.window.resizable(0, 0)
        self.window.config(bd=10, bg="azure")
        self.window.iconbitmap(r"c:/pythonProject/EXAMEN UNIDAD 2/icono.ico")

        titulo = Label(ventana_tarea, text="ANOTA TUS TAREAS", fg="black", bg="azure", font=("Arial", 20, "bold"), pady=10).pack()

        marco = LabelFrame(ventana_tarea, text="DATOS DE LA TAREA", bg="azure", font=("Arial", 15, "bold"), pady=5)
        marco.config(bd=2, bg="azure")
        marco.pack()


        label_asignatura= Label(marco, text="ASIGNATURA: ", bg="azure", font=("Ariual", 12, "bold")).grid(row=0, column=0,sticky='s', padx=5,pady=9)
        self.combo_asignatura = ttk.Combobox(marco,values=["POO", "CALCULO", "ALGEBRA", "CONTABILIDAD","PROBABILIDAD","QUIMICA"],width=22,font=("Arial", 12, "bold"), state="readonly")
        self.combo_asignatura.current(0)
        self.combo_asignatura.focus()
        self.combo_asignatura.grid(row=0, column=1, padx=5, pady=0)

        label_fecha = Label(marco, text="FECHA DE ENTREGA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.fecha = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.fecha.grid(row=1, column=1, padx=5, pady=8)

        label_puntaje = Label(marco, text="VALOR DE LA TAREA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=2, column=0,sticky='s', padx=5,pady=8)
        self.puntaje = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.puntaje.grid(row=2, column=1, padx=5, pady=8)

        label_descripcion = Label(marco, text="DESCRIPCIÓN: ", bg="azure", font=("Arial", 12, "bold")).grid(row=3, column=0,sticky='s',padx=5, pady=8)
        self.descripcion = Entry(marco, width=25, font=("Arial", 12, "bold"))
        self.descripcion.grid(row=3, column=1, padx=5, pady=8)

        frame_botones = Frame(ventana_tarea)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        boton_registrar = Button(frame_botones, text="AÑADIR",command=self.agregar_tareas, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="ELIMINAR", command=self.eliminar_asignatura,height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10,pady=15)
        boton_menu = Button(frame_botones, text="MENÚ PRINCIPAL", command=self.llamar_menu, height=2, width=15,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="SALIR", command=self.llamar_login, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=10,pady=15)

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
        self.Obtener_tareas()



    def Ejecutar_consulta(self, query, parameters=()):
            with sqlite3.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                result = cursor.execute(query, parameters)
                conexion.commit()
            return result

    def Validar_formulario_completo(self):
            if len(self.combo_asignatura.get()) != 0 and len(self.fecha.get()) != 0 and len(self.puntaje.get()) != 0 and  len(self.descripcion.get()) != 0:
                return True
            else:
                messagebox.showerror("ERROR", "Complete todos los campos del formulario")

    def Limpiar_formulario(self):
            self.combo_asignatura.delete(0, END)
            self.fecha.delete(0, END)
            self.puntaje.delete(0, END)
            self.descripcion.delete(0, END)

    def Obtener_tareas(self):
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            query = 'SELECT * FROM MISTAREAS ORDER BY asignatura desc'
            db_rows = self.Ejecutar_consulta(query)
            for row in db_rows:
                self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4]))

    def agregar_tareas(self):
            if self.Validar_formulario_completo():
                query = 'INSERT INTO MISTAREAS VALUES(NULL, ?, ?, ?, ?)'
                parameters = (self.combo_asignatura.get(), self.fecha.get(),self.puntaje.get(),self.descripcion.get())
                self.Ejecutar_consulta(query, parameters)
                messagebox.showinfo("REGISTRO EXITOSO", f'Tare registrado de la materia: {self.combo_asignatura.get()}')
                print('REGISTRADO')
            self.Limpiar_formulario()
            self.Obtener_tareas()

    def eliminar_asignatura(self):
            try:
                self.tree.item(self.tree.selection())['values'][0]
            except IndexError as e:
                messagebox.showerror("ERROR", "Porfavor selecciona un elemento")
                return
            dato = self.tree.item(self.tree.selection())['text']
            nombre = self.tree.item(self.tree.selection())['values'][0]
            query = "DELETE FROM MISTAREAS WHERE asignatura = ?"
            respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Seguro que desea eliminar esta tarea:?")
            if respuesta == 'yes':
                self.Ejecutar_consulta(query, (dato,))
                self.Obtener_tareas()
                messagebox.showinfo('ÉXITO', 'TAREAS HECHA :3')
            else:
                messagebox.showerror('ERROR', f'Error al eliminar la tarea')

    def llamar_login(self):
        ventana_tarea.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN UNIDAD 2/LOGIN.py'])

    def llamar_menu(self):
         ventana_tarea.destroy()
         call([sys.executable, 'c:/pythonProject/EXAMEN UNIDAD 2/MENU DESPEGABLE.py'])



if __name__ == '__main__':
    ventana_tarea = Tk()
    application = Tareas(ventana_tarea)
    ventana_tarea.mainloop()