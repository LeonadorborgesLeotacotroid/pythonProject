import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkComboBox
from tkcalendar import DateEntry

class VentanaPrincipal(CTk):
    global T
    T = 0

    def __init__(self):
            super().__init__()
            self.title("Ejemplo de ComboBox y Treeview")

            # Crear ComboBox
            opciones = ["INICIO", "COMPRA", "COSTO DE VENTAS", "DEVOLUCION S.C.", "DEVOLUCION S.V."]
            self.combobox = CTkComboBox(self, values=opciones, state="readonly")
            self.combobox.pack(pady=10)

            # Crear Treeview
            self.treeview = ttk.Treeview(self, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8), show="headings")
            self.treeview.pack()
            self.treeview.heading(0, text="Fecha de operacion")
            self.treeview.heading(1, text="Entradas")
            self.treeview.heading(2, text="Salidas")
            self.treeview.heading(3, text="Existencias")
            self.treeview.heading(4, text="Costo unitario")
            self.treeview.heading(5, text="Costo promedio")
            self.treeview.heading(6, text="Debe")
            self.treeview.heading(7, text="Haber")
            self.treeview.heading(8, text="Saldo")

            # Crear botón para abrir ventana
            self.btn_abrir_ventana = CTkButton(self, text="Abrir Ventana", command=self.abrir_ventana)
            self.btn_abrir_ventana.pack()
            self.btn_abrir_ventana = CTkButton(self, text="ELIMINAR", command=self.eliminar_renglon)
            self.btn_abrir_ventana.pack()

            self.btn_select_theme = CTkButton(self, text="Cambiar color del tema", command=self.Cambiar_tema)
            self.btn_select_theme.pack()

    def abrir_ventana(self):
        seleccion = self.combobox.get()

        if seleccion == "INICIO":
            ventana_opcion1 = VentanaOpcion1(self)
        elif seleccion == "COMPRA":
            ventana_opcion2 = VentanaOpcion2(self)
        elif seleccion == "COSTO DE VENTAS":
            ventana_opcion3 = VentanaOpcion3(self)
        elif seleccion == "DEVOLUCION S.C.":
            ventana_opcion4 = VentanaOpcion4(self)
        elif seleccion == "DEVOLUCION S.V.":
            ventana_opcion5 = VentanaOpcion5(self)
        elif seleccion == "":
            messagebox.showerror("ERROR","SELECCIONE UNA OPERACION")

    def eliminar_renglon(self):
        # Verificar si se seleccionó una fila
        seleccion = self.treeview.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, seleccione una fila.")
            return

        # Obtener todos los renglones del Treeview
        renglones = self.treeview.get_children()

        # Verificar si la fila seleccionada es la última fila
        if seleccion[-1] != renglones[-1]:
            messagebox.showerror("Error", "Por favor, seleccione la última fila.")
            return

        # Eliminar el último renglón del Treeview
        self.treeview.delete(seleccion[-1])

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

        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col1 = CTkLabel(self, text="Entradas:", text_color="Black")
        self.label_col1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col1 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col1.grid(row=0, column=1, padx=5, pady=5)

        self.label_col4 = CTkLabel(self, text="Costo unitario:", text_color="Black")
        self.label_col4.grid(row=1, column=0, padx=5, pady=5)
        self.entry_col4 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col4.grid(row=1, column=1, padx=5, pady=5)

        # Crear campo de fecha
        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self,state="readonly")
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        # Verificar que los campos no estén vacíos y que cumplan con las condiciones especificadas
        if not all([self.entry_col1.get(), self.entry_col4.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return

        if not all([self.validate_entry(self.entry_col1.get()), self.validate_entry(self.entry_col4.get())]):
            messagebox.showerror("Error",
                                 "Los campos deben cumplir con las condiciones especificadas en el método validate_entry.",
                                 parent=self)
            return
        col1 = float(self.entry_col1.get())
        col4 = float(self.entry_col4.get())
        col2 = 0
        col3 = col1
        col5 = 0
        col6 = float(col1) * float(col4)
        col7 = 0
        col8 = col6

        # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()

        # Format the date as a string
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired

        # Lógica para obtener col5
        if col3 != 0:
            col5 = float(col8) / float(col3)
        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end", values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8))

        self.destroy()

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False

class VentanaOpcion2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 2")

        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col1 = CTkLabel(self, text="Entradas:", text_color="Black")
        self.label_col1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col1 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col1.grid(row=0, column=1, padx=5, pady=5)

        self.label_col4 = CTkLabel(self, text="Costo unitario:", text_color="Black")
        self.label_col4.grid(row=1, column=0, padx=5, pady=5)
        self.entry_col4 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col4.grid(row=1, column=1, padx=5, pady=5)

        # Crear campo de fecha
        self.label_fecha = CTkLabel(self, text="Fecha:", text_color="Black")
        self.label_fecha.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Crear botón para guardar datos
        self.btn_guardar = CTkButton(self, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def guardar_datos(self):
        if not all([self.entry_col1.get(), self.entry_col4.get()]):
            messagebox.showerror("Error", "Ningún campo debe estar vacío.", parent=self)
            return
        selected_item = self.master.treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una fila.", parent=self)
            return

        col1 = self.entry_col1.get()
        col4 = self.entry_col4.get()
        col2 = 0
        col3 = float(col1) + float(self.master.treeview.item(self.master.treeview.focus())["values"][3])
        col5 = 0
        col6 = float(col1) * float(col4)
        col7 = 0
        col8 = col6 + float(self.master.treeview.item(self.master.treeview.focus())["values"][8])

        # Get the selected date from the DateEntry widget
        selected_date = self.date_entry.get_date()
        formatted_date = selected_date.strftime("%Y-%m-%d")  # Customize the format as desired
        # Lógica para obtener col5
        if col3 != 0:
            col5 = float(col8) / float(col3)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8))

        self.destroy()  # Cerrar ventana

    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False

class VentanaOpcion3(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 3")

        # Crear campos de entrada
        vcmd = (self.register(self.validate_entry), '%P')
        self.label_col2 = CTkLabel(self, text="Salidas:", text_color="Black")
        self.label_col2.grid(row=0, column=0, padx=5, pady=5)
        self.entry_col2 = CTkEntry(self, validate='key', validatecommand=vcmd)
        self.entry_col2.grid(row=0, column=1, padx=5, pady=5)

        # Crear campo de fecha
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

        col2 = self.entry_col2.get()
        col1 = 0
        col3 = float(self.master.treeview.item(self.master.treeview.focus())["values"][3]) - float(col2)
        col4 = self.master.treeview.item(self.master.treeview.focus())["values"][5]
        col5 = 0
        col6 = 0
        col7 = float(col2) * float(col4)
        col8 = float(self.master.treeview.item(self.master.treeview.focus())["values"][8]) - float(col7)
        selected_date = self.date_entry.get_date()

        selected_date = self.date_entry.get_date()
        formatted_date = selected_date.strftime("%Y-%m-%d")
        # Lógica para obtener col5
        if col3 != 0:
            col5 = float(col8) / float(col3)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8))
        self.destroy()
    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False

class VentanaOpcion4(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Opción 4")

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
        col2 = int(self.entry_col3.get())
        col1 = 0
        col3 = float(self.master.treeview.item(self.master.treeview.focus())["values"][3]) - float(col2)
        col4 = self.master.treeview.item(self.master.treeview.focus())["values"][5]
        col5 = 0
        col6 = 0
        col7 = float(col2) * float(col4)
        col8 = float(self.master.treeview.item(self.master.treeview.focus())["values"][8]) - float(col7)
        # Lógica para obtener col5
        selected_date = self.date_entry.get_date()

        formatted_date = selected_date.strftime("%Y-%m-%d")
        if col3 != 0:
            col5 = float(col8) / float(col3)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8))

        self.destroy()
    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 1000:
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
        self.label_col3 = CTkLabel(self, text="Entradas:", text_color="Black")
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
        col1 = int(self.entry_col3.get())
        col2 = 0
        col3 = float(self.master.treeview.item(self.master.treeview.focus())["values"][3]) + float(col1)
        col4 = self.master.treeview.item(self.master.treeview.focus())["values"][5]
        col5 = 0
        col7 = 0
        col6 = float(col1) * float(col4)
        col8 = float(self.master.treeview.item(self.master.treeview.focus())["values"][8]) + float(col6)
        selected_date = self.date_entry.get_date()

        formatted_date = selected_date.strftime("%Y-%m-%d")
        # Lógica para obtener col5
        if col3 != 0:
            col5 = float(col8) / float(col3)

        # Agregar datos al Treeview en la ventana principal
        ventana_principal = self.master
        ventana_principal.treeview.insert("", "end",values=(formatted_date, col1, col2, col3, col4, col5, col6, col7, col8))
        self.destroy()
    def validate_entry(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) > 0 and int(new_text) <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False


ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()