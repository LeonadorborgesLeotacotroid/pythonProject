import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter
import mysql.connector
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox
from tkcalendar import DateEntry

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="productos",
    buffered=True
)

T = 0

class VentanaPrincipal(CTk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de ComboBox y Treeview")
        self.ventana_abierta = False

        # Crear ComboBox
        opciones = ["INICIO", "COMPRA", "COSTO DE VENTAS", "DEVOLUCION S.C.", "DEVOLUCION S.V."]
        self.combobox = CTkComboBox(self, values=opciones, state="readonly")
        self.combobox.pack(pady=10)

        # Crear Treeview
        self.treeview = ttk.Treeview(self, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings")
        self.treeview.pack()
        self.treeview.heading(0, text="Fecha de operacion")
        self.treeview.heading(1, text="Tipo de Operacion")
        self.treeview.heading(2, text="Entradas")
        self.treeview.heading(3, text="Salidas")
        self.treeview.heading(4, text="Existencias")
        self.treeview.heading(5, text="Costo Unitario")
        self.treeview.heading(6, text="Costo Promedio")
        self.treeview.heading(7, text="Debe")
        self.treeview.heading(8, text="Haber")
        self.treeview.heading(9, text="Saldo")

        self.actualizar_treeview()

        # Crear botón para abrir ventana
        self.btn_abrir_ventana = CTkButton(self, text="Abrir Ventana", command=self.abrir_ventana)
        self.btn_abrir_ventana.pack()
        self.btn_abrir_ventana = CTkButton(self, text="ELIMINAR", command=self.eliminar_renglon)
        self.btn_abrir_ventana.pack()

        self.btn_select_theme = CTkButton(self, text="Cambiar color del tema", command=self.Cambiar_tema)
        self.btn_select_theme.pack()

    def actualizar_treeview(self):
        self.treeview.delete(*self.treeview.get_children())  # Limpiar el Treeview

        seleccionar = "select * from productos where usuario = 'av' and contraseña = 'a' and producto = ''"
        ta = bd.cursor()
        ta.execute(seleccionar)
        resultado = ta.fetchall()

        for materias in resultado:
            if not isinstance(materias, tuple):
                continue
            identificador = f"{materias[0]}_{materias[1]}"
            self.treeview.insert(parent='', index='end', iid=identificador, values=(
                materias[4], materias[5], materias[6], materias[7], materias[8], materias[9], materias[10], materias[11],
                materias[12], materias[13]), tags="CustomCell")

        ta.close()

    def abrir_ventana(self):
        if self.ventana_abierta:
            messagebox.showerror("Error", "Ya hay una ventana abierta.")
            return

        seleccion = self.combobox.get()

        if seleccion == "INICIO":
            ventana_opcion1 = VentanaOpcion1(self)
            ventana_opcion1.protocol("WM_DELETE_WINDOW",
                                     lambda: [ventana_opcion1.destroy(), setattr(self, 'ventana_abierta', False)])
            self.ventana_abierta = True
        elif seleccion == "COMPRA":
            ventana_opcion2 = VentanaOpcion2(self)
            ventana_opcion2.protocol("WM_DELETE_WINDOW",
                                     lambda: [ventana_opcion2.destroy(), setattr(self, 'ventana_abierta', False)])
            self.ventana_abierta = True
        elif seleccion == "COSTO DE VENTAS":
            ventana_opcion3 = VentanaOpcion3(self)
            ventana_opcion3.protocol("WM_DELETE_WINDOW",
                                     lambda: [ventana_opcion3.destroy(), setattr(self, 'ventana_abierta', False)])
            self.ventana_abierta = True
        elif seleccion == "DEVOLUCION S.C.":
            ventana_opcion4 = VentanaOpcion4(self)
            ventana_opcion4.protocol("WM_DELETE_WINDOW",
                                     lambda: [ventana_opcion4.destroy(), setattr(self, 'ventana_abierta', False)])
            self.ventana_abierta = True
        elif seleccion == "DEVOLUCION S.V.":
            ventana_opcion5 = VentanaOpcion5(self)
            ventana_opcion5.protocol("WM_DELETE_WINDOW",
                                     lambda: [ventana_opcion5.destroy(), setattr(self, 'ventana_abierta', False)])
            self.ventana_abierta = True

    def eliminar_renglon(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "No se ha seleccionado ningún renglón.")
            return

        values = self.treeview.item(selected_item)["values"]
        fecha_operacion = values[0]  # Obtener la fecha de operación (columna 0)

        eliminar_query = "DELETE FROM productos WHERE fecha = %s"
        eliminar_data = (fecha_operacion,)
        cursor = bd.cursor()
        cursor.execute(eliminar_query, eliminar_data)
        bd.commit()
        cursor.close()

        # Eliminar el ítem seleccionado del Treeview
        self.treeview.delete(selected_item)
        messagebox.showinfo("Eliminado", "El renglón ha sido eliminado de la base de datos.")
    def Cambiar_tema(self):
        global T
        T = T + 1
        if T % 2 != 0:
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("Dark")


class VentanaOpcion1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 1")
        self.ventana_abierta = False

        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col2 = CTkLabel(self, text="Entradas:", text_color="Black")
        self.label_col2.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col2 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col2.grid(row=0, column=1, padx=5, pady=5)

        self.label_col5 = CTkLabel(self, text="Costo unitario:", text_color="Black")
        self.label_col5.grid(row=1, column=0, padx=5, pady=5)
        self.entry_col5 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col5.grid(row=1, column=1, padx=5, pady=5)

        # Crear campo de fecha
        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self, state="readonly")
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        # Verificar que los campos no estén vacíos y que cumplan con las condiciones especificadas
        if not all([self.entry_col2.get(), self.entry_col5.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        col1 = "INICIO"
        col2 = float(self.entry_col2.get())
        col3 = 0
        col4 = col2
        col5 = float(self.entry_col5.get())
        col6 = 0
        col7 = float(col2) * float(col5)
        col8 = "-----"
        col9 = col7  # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()

        # Format the date as a string
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired

        # Lógica para obtener col6
        if col4 != 0:
            col6 = float(col9) / float(col4)
        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",
                                          values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9))

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES ('av', 'a', '', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        bd.commit()
        ta.close()
        self.master.ventana_abierta = False
        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 10000:
                return True
            else:
                return False
        except ValueError:
            return False


class VentanaOpcion2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 2")
        self.ventana_abierta = False
        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col2 = CTkLabel(self, text="Entradas:", text_color="Black")
        self.label_col2.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col2 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col2.grid(row=0, column=1, padx=5, pady=5)

        self.label_col5 = CTkLabel(self, text="Costo unitario:", text_color="Black")
        self.label_col5.grid(row=1, column=0, padx=5, pady=5)
        self.entry_col5 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col5.grid(row=1, column=1, padx=5, pady=5)

        # Crear campo de fecha
        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        if not all([self.entry_col2.get(), self.entry_col5.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        selected_item = self.master.treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una fila.", parent=self)
            return
        col1 = "COMPRA"
        col2 = self.entry_col2.get()
        col5 = self.entry_col5.get()
        col3 = 0
        col4 = float(col2) + float(self.master.treeview.item(self.master.treeview.focus())["values"][4])
        col6 = 0
        col7 = float(col2) * float(col5)
        col8 = 0
        col9 = col7 + float(self.master.treeview.item(self.master.treeview.focus())["values"][9])

        # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired
        # Lógica para obtener col5
        if col4 != 0:
            col6 = float(col9) / float(col4)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",
                                          values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9))
        self.master.ventana_abierta = False

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES ('av', 'a', '', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        bd.commit()
        ta.close()

        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 10500:
                return True
            else:
                return False
        except ValueError:
            return False


class VentanaOpcion3(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 3")
        self.ventana_abierta = False
        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col3 = CTkLabel(self, text="Salidas:", text_color="Black")
        self.label_col3.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col3 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col3.grid(row=0, column=1, padx=5, pady=5)

        # Crear campo de fecha
        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        if not all([self.entry_col3.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        selected_item = self.master.treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una fila.", parent=self)
            return
        col1 = "COSTO DE VENTAS"
        col3 = self.entry_col3.get()
        col2 = 0
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][4]) - float(col3)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][6]
        col6 = 0
        col7 = 0
        col8 = float(col3) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][9]) - float(col8)
        selected_date = self.date_entry.get_date()

        selected_date = self.date_entry.get_date()
        formatted_date = selected_date.strftime("%Y-%m-%d")
        # Lógica para obtener col5
        if col4 != 0:
            col6 = float(col9) / float(col4)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",
                                          values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9))
        self.master.ventana_abierta = False

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES ('av', 'a', '', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        bd.commit()
        ta.close()

        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 10500:
                return True
            else:
                return False
        except ValueError:
            return False


class VentanaOpcion4(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 4")
        self.ventana_abierta = False
        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col3 = CTkLabel(self, text="Salidas:", text_color="Black")
        self.label_col3.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col3 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col3.grid(row=0, column=1, padx=5, pady=5)

        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        if not all([self.entry_col3.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        selected_item = self.master.treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una fila.", parent=self)
            return
        col1 = "DEVOLUCION S/C"
        col3 = int(self.entry_col3.get())
        col2 = 0
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][4]) - float(col3)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][5]
        col6 = 0
        col7 = 0
        col8 = float(col3) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][9]) - float(col8)

        selected_date = self.date_entry.get_date()

        formatted_date = selected_date.strftime("%Y-%m-%d")
        if col4 != 0:
            col6 = float(col9) / float(col4)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",
                                          values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9))

        self.master.ventana_abierta = False

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES ('av', 'a', '', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        bd.commit()
        ta.close()

        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 10500:
                return True
            else:
                return False
        except ValueError:
            return False


class VentanaOpcion5(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 5")

        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col2 = CTkLabel(self, text="Entradas:", text_color="Black")
        self.label_col2.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col2 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col2.grid(row=0, column=1, padx=5, pady=5)

        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        if not all([self.entry_col2.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        selected_item = self.master.treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una fila.", parent=self)
            return
        col1 = "DEVOLUCION S/V"
        col2 = int(self.entry_col2.get())
        col3 = 0
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][4]) + float(col2)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][6]
        col6 = 0
        col8 = 0
        col7 = float(col2) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][9]) + float(col7)
        selected_date = self.date_entry.get_date()

        formatted_date = selected_date.strftime("%Y-%m-%d")
        # Lógica para obtener col5
        if col4 != 0:
            col6 = float(col9) / float(col4)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",
                                          values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9))
        self.master.ventana_abierta = False

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES ('av', 'a', '', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        bd.commit()
        ta.close()

        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 10500:
                return True
            else:
                return False
        except ValueError:
            return False


ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()