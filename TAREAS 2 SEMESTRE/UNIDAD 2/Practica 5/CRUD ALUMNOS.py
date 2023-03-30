import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
# Python image Library

import sqlite3



class Maestro:
    db_name = 'database_proyecto.db'

    def __init__(self, ventana_profe):
        self.window = ventana_profe
        self.window.title("APLICACION")
        self.window.geometry("800x670")
        self.window.resizable(0, 0)
        self.window.config(bd=10)

        "--------------- Titulo --------------------"
        titulo = Label(ventana_profe, text="REGISTRO DE MAESTROS", fg="black",
                       font=("Comic Sans", 17, "bold"), pady=10).pack()


        "--------------- Frame marco --------------------"
        marco = LabelFrame(ventana_profe, text="Datos del docente", font=("Comic Sans", 10, "bold"), pady=5)
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_codigo = Label(marco, text="Codigo: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0,
                                                                                                        sticky='s',
                                                                                                        padx=5, pady=8)
        self.codigo = Entry(marco, width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)

        label_nombre = Label(marco, text="Nombre docente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0,
                                                                                                        sticky='s',
                                                                                                        padx=5, pady=8)
        self.nombre = Entry(marco, width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)

        label_academia = Label(marco, text="Academia: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0,
                                                                                                 sticky='s', padx=5,
                                                                                                 pady=9)
        self.combo_academia = ttk.Combobox(marco,
                                            values=["Sistemas", "Electromecanica", "Administracion", "Renovables", "Animacion"],
                                            width=22, state="readonly")
        self.combo_academia.current(0)
        self.combo_academia.grid(row=2, column=1, padx=5, pady=0)

        label_edad = Label(marco, text="Edad: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2,
                                                                                               sticky='s', padx=5,
                                                                                               pady=8)
        self.edad = Entry(marco, width=25)
        self.edad.grid(row=0, column=3, padx=5, pady=8)

        label_sueldo = Label(marco, text="Sueldo: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2,
                                                                                                 sticky='s', padx=5,
                                                                                                 pady=8)
        self.sueldo= Entry(marco, width=25)
        self.sueldo.grid(row=1, column=3, padx=5, pady=8)

        label_descripcion = Label(marco, text="Descripcion: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=2,
                                                                                                     sticky='s',
                                                                                                     padx=10, pady=8)
        self.descripcion = Entry(marco, width=25)
        self.descripcion.grid(row=2, column=3, padx=10, pady=8)

        "--------------- Frame botones --------------------"
        frame_botones = Frame(ventana_profe)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.Agregar_maestro, height=2, width=10,
                                 bg="green", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=1, padx=10,
                                                                                               pady=15)
        boton_eliminar = Button(frame_botones, text="ELIMINAR", command=self.Eliminar_maestro, height=2, width=10,bg="red", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, padx=10,pady=15)
        boton_registrarmaestros = Button(frame_botones, text="REGISTRAR ALUMNOS", command=self.llamar_maestro,
                                         height=5, width=15,bg="green", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=3,padx=10,pady=15)
        boton_salir = Button(frame_botones, text="SALIR", command=self.salir_registro, height=2, width=10,
                             bg="red", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=4, padx=10,
                                                                                         pady=15)

        "--------------- Tabla --------------------"
        self.tree = ttk.Treeview(height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))
        self.tree.heading("#0", text='CODIGO', anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)

        self.tree.heading("columna1", text='NOMBRE', anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna2", text='ACADEMIA', anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna3", text='EDAD', anchor=CENTER)
        self.tree.column("columna3", width=70, minwidth=60, stretch=NO)

        self.tree.heading("columna4", text='SUELDO', anchor=CENTER)
        self.tree.column("columna4", width=70, minwidth=60, stretch=NO)

        self.tree.heading("columna5", text='Descripcion', anchor=CENTER)

        self.tree.pack()

        self.Obtener_maestros()

    "--------------- CRUD --------------------"

    def Obtener_maestros(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM Maestros ORDER BY nombre desc'
        db_rows = self.Ejecutar_consulta(query)
        for row in db_rows:
            self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))

    def Agregar_maestro(self):
        if self.Validar_formulario_completo():
            query = 'INSERT INTO Maestros VALUES(NULL, ?, ?, ?, ?, ?, ?)'
            parameters = (self.codigo.get(), self.nombre.get(), self.combo_academia.get(), self.edad.get(), self.sueldo.get(),self.descripcion.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'maestro  registrado: {self.nombre.get()}')
            print('REGISTRADO')
        self.Limpiar_formulario()
        self.Obtener_maestros()

    def Eliminar_maestro(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            messagebox.showerror("ERROR", "Porfavor selecciona un elemento")
            return
        dato = self.tree.item(self.tree.selection())['text']
        nombre = self.tree.item(self.tree.selection())['values'][0]
        query = "DELETE FROM Maestros WHERE codigo = ?"
        respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Seguro que desea eliminar al maestro: {nombre}?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query, (dato,))
            self.Obtener_maestros()
            messagebox.showinfo('EXITO', f'Maestro eliminado: {nombre}')
        else:
            messagebox.showerror('ERROR', f'Error al eliminar al maestro: {nombre}')



    "--------------- OTRAS FUNCIONES --------------------"

    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
        return result

    def Validar_formulario_completo(self):
        if len(self.codigo.get()) != 0 and len(self.nombre.get()) != 0 and len(self.combo_academia.get()) != 0 and len(
                self.edad.get()) != 0 and len(self.sueldo.get()) != 0 and len(self.descripcion.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR", "Complete todos los campos del formulario")

    def Limpiar_formulario(self):
        self.codigo.delete(0, END)
        self.nombre.delete(0, END)
        self.edad.delete(0, END)
        self.sueldo.delete(0, END)
        self.descripcion.delete(0, END)

    def llamar_maestro(self):
     ventana_profe.destroy()
     call([sys.executable,'C:/pythonProject/TAREAS 2 SEMESTRE/UNIDAD 2/Practica 5/CRUD PRINCIPAL.py'])

    def salir_registro(self):
     ventana_profe.destroy()





if __name__ == '__main__':
    ventana_profe = Tk()
    application = Maestro(ventana_profe)
    ventana_profe.mainloop()