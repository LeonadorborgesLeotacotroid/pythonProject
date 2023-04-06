from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    # conexion a la base de datos
    db_name = 'database.db'

    def __init__(self, window):

        self.wind = window
        self.wind.title('ALUMNOS  CRUD')

        # crear frame
        frame = LabelFrame(self.wind, text = 'Registrar alumno')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        Label(frame, text = 'Matricula: ').grid(row = 2, column = 0)
        self.matricula = Entry(frame)
        self.matricula.grid(row = 2, column = 1)

        #BTONO REGISTRAR
        ttk.Button(frame, text = 'Registrar', command = self.add_alumnos).grid(row = 3, columnspan = 2, sticky = W + E)


        self.mensaje = Label(text = '', fg = 'red')
        self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Matricula', anchor = CENTER)


        ttk.Button(text = 'ELIMINAR', command = self.delete_alumnos).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDITAR', command = self.edit_alumnos).grid(row = 5, column = 1, sticky = W + E)
        self.get_alumnos()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_alumnos(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.matricula.get()) != 0

    def add_alumnos(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.matricula.get())
            self.run_query(query, parameters)
            self.mensaje['text'] = 'Alumnos agregado con exito .format(self.name.get())'
            self.name.delete(0, END)
            self.matricula.delete(0, END)
        else:
            self.mensaje['text'] = 'Se requiere el nombre y matricula del alumno'
        self.get_alumnos()

    def delete_alumnos(self):
        self.mensaje['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor seleccione un registro'
            return
        self.mensaje['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.mensaje['text'] = 'Alumno eliminado con exito'.format(name)
        self.get_alumnos()

    def edit_alumnos(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor seleccione un registro'
            return
        name = self.tree.item(self.tree.selection())['text']
        matricula = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Alumno Editar'
        # NOMBRE VIEJO
        Label(self.edit_wind, text = 'Nombre Anterior:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # NOMBRE NUEVO
        Label(self.edit_wind, text = 'Nombre Nuevo').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        #MATRICULA VIEJA
        Label(self.edit_wind, text = 'Matricula vieja:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = matricula), state = 'readonly').grid(row = 2, column = 2)
        #MATTRICULA NUEVA
        Label(self.edit_wind, text = 'Matricula Nueva:').grid(row = 3, column = 1)
        new_matricula= Entry(self.edit_wind)
        new_matricula.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, new_matricula.get(), matricula)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_matricula, matricula):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_matricula,name, matricula)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = "DATOS ACTUALIZADOS CON EXITO".format(name)
        self.get_alumnos()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()