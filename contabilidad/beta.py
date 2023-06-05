from tkinter import ttk, messagebox
from typing import Optional, Tuple, Union
from tkcalendar import DateEntry
import customtkinter
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox, CTkFrame
from tkinter import *
import mysql.connector
import tkinter as tk
import pandas as pd
from openpyxl import Workbook

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

        def volver():
            self.withdraw()
            lg.deiconify()

        self.title("Ejemplo de ComboBox y Treeview")
        self.geometry("1200x570")
        self.resizable(0, 480)
        self.ventana_abierta = False

        self.frame_top = CTkFrame(self, width=27, height=50)
        self.frame_top.pack(side=tk.TOP, fill=tk.BOTH)

        opciones = ["INICIO", "COMPRA", "COSTO DE VENTAS", "DEVOLUCION S.C.", "DEVOLUCION S.V."]
        self.combobox = CTkComboBox(self.frame_top, values=opciones, state="readonly")
        self.combobox.place(x=25, y=10)
        self.label = CTkLabel(self.frame_top, text="OPERACION A ELEGIR ")
        self.label.place(x=10, y=10)

        self.btn_abrir_ventana = CTkButton(self.frame_top, text="ABRIR VENTANA", command=self.abrir_ventana)
        self.btn_abrir_ventana.place(x=450, y=10)

        self.btn_select_theme = CTkButton(self.frame_top, text="ELIMINAR", command=self.eliminar_renglon,fg_color=("#DB3E39","#821D1A"))
        self.btn_select_theme.place(x=600, y=10)

        self.btn_excel = CTkButton(self.frame_top, text="DESCARGAR EXCEL", command=self.excel,bg_color="limegreen", fg_color=("#32CD32"))
        self.btn_excel.place(x=1000, y=10)

        self.treeview = ttk.Treeview(self, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings")
        self.treeview.pack(pady=50)

        self.treeview.column(0, width=25, stretch=False)
        self.treeview.column(1, width=100)
        self.treeview.column(2, width=100)
        self.treeview.column(3, width=75)
        self.treeview.column(4, width=75)
        self.treeview.column(5, width=100)
        self.treeview.column(6, width=100)
        self.treeview.column(7, width=135)
        self.treeview.column(8, width=75)
        self.treeview.column(9, width=75)
        self.treeview.column(10, width=75)

        self.treeview.heading(0, text="ID")
        self.treeview.heading(1, text="FECHA DE OPERACIÓN")
        self.treeview.heading(2, text="TIPO DE OPERACIÓN")
        self.treeview.heading(3, text="ENTRADAS")
        self.treeview.heading(4, text="SALIDAS")
        self.treeview.heading(5, text="EXISTENCIAS")
        self.treeview.heading(6, text="COSTO UNITARIO")
        self.treeview.heading(7, text="COSTO PROMEDIO")
        self.treeview.heading(8, text="DEBE")
        self.treeview.heading(9, text="HABER")
        self.treeview.heading(10, text="SALDO")

        self.actualizar_treeview()

        self.frame_bottom = CTkFrame(self,width=47, height=80)
        self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.btn_eliminar = CTkButton(self.frame_bottom, text="COLOR DEL TEMA", command=self.Cambiar_tema)
        self.btn_eliminar.place(x=450, y=15)

        self.btn_regresar = CTkButton(self.frame_bottom, text="SALIR", command=volver,fg_color=("#DB3E39","#821D1A"))
        self.btn_regresar.place(x=600, y=15)

    def actualizar_treeview(self):
        self.treeview.delete(*self.treeview.get_children())

        seleccionar = "select * from productos where usuario = %s and contraseña = %s and producto = %s"
        datos = (usuario, contraseña, Product_entry.get())
        ta = bd.cursor()
        ta.execute(seleccionar, datos, )
        resultado = ta.fetchall()

        for materias in resultado:
            if not isinstance(materias, tuple):
                continue
            identificador = f"{materias[0]}_{materias[1]}"
            self.treeview.insert(parent='', index='end', iid=identificador, values=(
                materias[0], materias[4], materias[5], materias[6], materias[7], materias[8], materias[9], materias[10],
                materias[11],
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
        elif seleccion == "":
            messagebox.showerror("ERROR","SELECCIONA UNA OPERACION")

    def eliminar_renglon(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "No se ha seleccionado ningún renglón.")
            return

        selected_index = self.treeview.index(selected_item)

        total_rows = self.treeview.get_children()

        if selected_index != len(total_rows) - 1:
            messagebox.showerror("Error", "Solo se puede eliminar la última fila.")
            return

        values = self.treeview.item(selected_item)["values"]
        numero_operacion = values[0]

        eliminar_query = "DELETE FROM productos WHERE numeroop = %s"
        eliminar_data = (numero_operacion,)
        cursor = bd.cursor()
        cursor.execute(eliminar_query, eliminar_data)
        bd.commit()
        cursor.close()

        self.treeview.delete(selected_item)
        messagebox.showinfo("Eliminado", "El renglón ha sido eliminado de la base de datos.")

    def Cambiar_tema(self):
        global T
        T = T + 1
        if T % 2 != 0:
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("Dark")

    def excel(self):
        datos = pd.DataFrame(columns=[
            "ID", "Fecha de operacion", "Tipo de Operacion", "Entradas", "Salidas",
            "Existencias", "Costo Unitario", "Costo Promedio", "Debe", "Haber", "Saldo"
        ])
        for x in self.treeview.get_children():
            valores = self.treeview.item(x, "values")
            datos.loc[len(datos)] = valores
        workbook = Workbook()
        hoja1 = workbook.active

        columnas = ["ID", "Fecha de operacion", "Tipo de Operacion", "Entradas", "Salidas",
                    "Existencias", "Costo Unitario", "Costo Promedio", "Debe", "Haber", "Saldo"]
        hoja1.append(columnas)

        for _, row in datos.iterrows():
            hoja1.append(row.tolist())
        ci = messagebox.askyesno("Renombre excel",
                                 "Esta seguro de querer generar un otro excel\ntenga en cuenta que si no se modifica el\n nombre de uno antes generado, el excel se\nsobre escribira ")
        if ci:
            workbook.save(usuario + "_promedios_" + Product_entry.get() + "_.xlsx")

            messagebox.showinfo("Exportar a Excel", "Los datos se han exportado exitosamente a un archivo Excel.")
        else:
            return


class VentanaRegistro(CTk, Toplevel):
    def __init__(self):
        super().__init__()

        def volver():
            self.withdraw()
            lg.deiconify()

        def registro_():

            usuario = self.entry_usuario.get()
            contraseña = self.entry_contraseña.get()

            if not usuario or not contraseña:
                messagebox.showinfo(message="Usuario o contraseña no pueden estar vacíos")
                return

            seleccionar = "SELECT * FROM productos WHERE usuario = %s"
            ta = bd.cursor()
            ta.execute(seleccionar, (usuario,))
            resultado = ta.fetchone()

            if resultado:
                messagebox.showinfo(title="Duplicado", message="El usuario que intenta registrar ya existe")
            else:
                registrar = bd.cursor()
                regist = "INSERT INTO productos (usuario, contraseña, producto) VALUES (%s, %s, %s)"
                for x in range(1, 3):
                    rar = (usuario, contraseña, "Producto " + str(x))
                    registrar.execute(regist, rar)
                bd.commit()
                messagebox.showinfo(title="Registro exitoso", message="El usuario ha sido registrado correctamente")
                volver()
                ta.close()

        lg.withdraw()

        self.title("Registro")
        self.geometry('700x500')
        self.resizable(0, 0)

        self.frame = CTkFrame(self, fg_color="DeepSkyBlue4", border_color="DeepSkyBlue4", width=327, height=550)
        self.frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.label = CTkLabel(self, text="REGISTRO", text_color="white", font=('Arial', 30, 'bold',))
        self.label.pack(padx=60, pady=10)

        self.marco = LabelFrame(self.frame, text="INGRESE SUS DATOS", bg="DeepSkyBlue4",
                                font=("Comic Sans", 15, "bold"))
        self.marco.config(padx=30, pady=10, bd=5)
        self.marco.pack()

        self.label_usuario = CTkLabel(self.marco, text="USUARIO", text_color="BLACK")
        self.label_usuario.grid(row=1, column=1, pady=4)

        vcmd = (self.register(self.validate_username), '%P')
        self.entry_usuario = CTkEntry(self.marco, text_color="BLACK", validate='key', validatecommand=vcmd)
        self.entry_usuario.grid(row=1, column=2, pady=25)

        self.label_usuario = CTkLabel(self.marco, text="CONTRASEÑA", text_color="BLACK")
        self.label_usuario.grid(row=2, column=1, pady=4)

        vcmd = (self.register(self.validate_password), '%P')
        self.entry_contraseña = CTkEntry(self.marco, text_color="BLACK", validate='key', validatecommand=vcmd)
        self.entry_contraseña.grid(row=2, column=2, pady=7)

        self.but_on = CTkButton(self.marco, text="REGISTRAR", command=registro_)
        self.but_on.grid(row=3, column=1, pady=55)

        self.button = CTkButton(self.marco, text="REGRESAR", command=volver)
        self.button.grid(row=3, column=2, pady=8)

        self.mainloop()

    def validate_username(self, new_text):
        if not new_text:
            return True

        if new_text.isalpha() and len(new_text) <= 15:
            return True
        return False



    def validate_password(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) >= 0 and len(new_text) <= 8:
                return True
            else:
                return False
        except ValueError:
            return False



class VentanaOpcion1(tk.Toplevel):
    def __init__(self, master):
        self.master = master
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
        col8 = 0
        col9 = col7  # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()

        # Format the date as a string
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired

        # Lógica para obtener col6
        if col4 != 0:
            col6 = float(col9) / float(col4)
        # Agregar datos al Treeview en la ventana principal
        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (
        usuario, contraseña, Product_entry.get(), formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        self.master.actualizar_treeview()
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
        self.master = master
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
        col4 = float(col2) + float(self.master.treeview.item(self.master.treeview.focus())["values"][5])
        col6 = 0
        col7 = float(col2) * float(col5)
        col8 = 0
        col9 = col7 + float(self.master.treeview.item(self.master.treeview.focus())["values"][10])

        # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired
        # Lógica para obtener col5
        if col4 != 0:
            col6 = float(col9) / float(col4)

        ta = bd.cursor()
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (
        usuario, contraseña, Product_entry.get(), formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        self.master.actualizar_treeview()
        bd.commit()
        ta.close()

        self.master.ventana_abierta = False
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
        self.master = master
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
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][5]) - float(col3)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][7]
        col6 = 0
        col7 = 0
        col8 = float(col3) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][10]) - float(col8)
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
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (
        usuario, contraseña, Product_entry.get(), formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        self.master.actualizar_treeview()
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
        self.master = master
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
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][5]) - float(col3)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][6]
        col6 = 0
        col7 = 0
        col8 = float(col3) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][10]) - float(col8)

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
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (
        usuario, contraseña, Product_entry.get(), formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        self.master.actualizar_treeview()
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
        self.master = master
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
        col4 = float(self.master.treeview.item(self.master.treeview.focus())["values"][5]) + float(col2)
        col5 = self.master.treeview.item(self.master.treeview.focus())["values"][7]
        col6 = 0
        col8 = 0
        col7 = float(col2) * float(col5)
        col9 = float(self.master.treeview.item(self.master.treeview.focus())["values"][10]) + float(col7)
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
        datos = "INSERT INTO productos (usuario, contraseña, producto, fecha, operacion, entradas, salidas, existencias, costounitario, costopromedio, debe, haber, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        llenar = (
        usuario, contraseña, Product_entry.get(), formatted_date, col1, col2, col3, col4, col5, col6, col7, col8, col9)
        ta.execute(datos, llenar, )
        self.master.actualizar_treeview()
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
def inicio():
    global usuario
    global contraseña

    usuario = matricula_entry.get()
    contraseña = password_entry.get()


    if not usuario or not contraseña:
        messagebox.showinfo(message="Usuario o contraseña no pueden estar vacíos")
        return

    seleccionar = "select * from productos where usuario = %s and contraseña = %s and producto = %s"
    ta = bd.cursor()
    ta.execute(seleccionar, (usuario, contraseña, Product_entry.get(),))
    resultado = ta.fetchone()

    if not resultado:
        messagebox.showinfo(message="Error usuario y/o contraseña")
        return

    elif resultado[1] == usuario and resultado[2] != contraseña:
        messagebox.showinfo(message="Contraseña incorrecta")
        return

    elif resultado[1] == usuario and resultado[2] == contraseña:
        lg.withdraw()
        a = VentanaPrincipal()
        a.mainloop()
        ta.close()



def registros():
    VentanaRegistro()

def validate_employee_name(new_text):

    if not new_text:
        return True
    if new_text.isalpha() and len(new_text) <= 15:
        return True
    return False

def validate_password(new_text):
        if not new_text:
            return True
        try:
            if int(new_text) >= 0 and len(new_text) <= 8:
                return True
            else:
                return False
        except ValueError:
            return False


lg = customtkinter.CTk()
lg.geometry('700x500')
lg.config(bg="black")
lg.title("INICIO")
lg.resizable(False, False)
# lg.iconbitmap(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad/tecnologia-financiera.ico")

# img = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad/FUTURE.png")
# render = ImageTk.PhotoImage(img)
# label_imagen = tk.Label(lg, image=render)
# label_imagen.image = render
# label_imagen.config(bg="black")
# label_imagen.place(y=0, x=0)

# Insertamos una imagen que no es porque le queda una marca de agua horrible
# img = PhotoImage(file=r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad\FUTURE.png")
# label_img = customtkinter.CTkLabel(master=lg, image=img,text="")
# label_img.place(y=0, x=0)

# Creamos un frame
frame = customtkinter.CTkFrame(master=lg, fg_color="DeepSkyBlue4", border_color="DeepSkyBlue4", width=327, height=550)
frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# Dentro del frame
label = customtkinter.CTkLabel(master=frame, text="BIENVENIDO", bg_color="DeepSkyBlue4", text_color="black",
                               font=('Arial', 30, 'bold',))
label.pack(padx=60, pady=10)

# imagen_registro = Image.open(r"C:\Users\miche\PycharmProjects\PYCHARMich\Contabilidad\LOGO.png")
# nueva_imagen = imagen_registro.resize((200, 200))
# render = ImageTk.PhotoImage(nueva_imagen)
# label_imagen = Label(master=frame, image=render)
# label_imagen.image = render
# label_imagen.config(bg="DeepSkyBlue4")
# label_imagen.pack(pady=10, padx=0, ipadx=0)

marco = LabelFrame(master=frame, text="INICIA SESIÓN", bg="DeepSkyBlue4", font=("Comic Sans", 15, "bold"))
marco.config(padx=30, pady=10, bd=5)
marco.pack()

matricula_label = tk.Label(marco, text="NOMBRE DEL EMPLEADO:", bg="DeepSkyBlue4", font=("Arial", 12, "bold"))
matricula_label.grid(row=1, column=1, padx=5, pady=8)

vcmd = (marco.register(validate_employee_name), '%P')
matricula_entry = tk.Entry(marco, validate="key", validatecommand=vcmd, width=20, font=("Arial", 12))
matricula_entry.grid(row=1, column=2, padx=5, pady=8)

password_label = tk.Label(marco, text="CONTRASEÑA:", bg="DeepSkyBlue4", font=("Arial", 12, "bold"))
password_label.grid(row=2, column=1, padx=5, pady=8)

vcmd1 = (marco.register(validate_password), '%P')
password_entry = tk.Entry(marco, show="*", validate="key", validatecommand=vcmd1, width=20, font=("Arial", 12))
password_entry.grid(row=2, column=2, padx=5, pady=8)

Product_label = tk.Label(marco, text="PRODUCTO:", bg="DeepSkyBlue4", font=("Arial", 12, "bold"))
Product_label.grid(row=3, column=1, padx=5, pady=8)

opciones_ = ["Producto 1", "Producto 2"]

Product_entry = CTkComboBox(marco, width=150, values=opciones_)
Product_entry.grid(row=3, column=2, padx=5, pady=8)

frame_botones = Frame(master=frame)
frame_botones.config(bg="DeepSkyBlue4")
frame_botones.pack(pady=10)



login_button = tk.Button(frame_botones, text="INICIAR SESIÓN", height=2, width=15, bg="cyan3", fg="black",
                         font=("Arial", 12, "bold"), command=inicio)
login_button.grid(row=3, column=1, padx=5, pady=8)



register_button = tk.Button(frame_botones, text="REGISTRARSE", height=2, width=15, bg="cyan3", fg="black",
                            font=("Arial", 12, "bold"), command=registros)
register_button.grid(row=3, column=2, padx=5, pady=8)

usuario = None
contraseña = None





if __name__ == "__main__":
    lg.mainloop()