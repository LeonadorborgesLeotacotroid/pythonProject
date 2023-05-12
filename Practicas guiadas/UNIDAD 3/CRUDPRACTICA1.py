#Leonardo Melchor Borges Pech
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS datos (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        estado VARCHAR(255),
        checkbox_value INT
    );
""")

connection.close()

"------------EN ESTE APARTADO SE PROGRAMA UN DEF PARA QUE SE PUEDA INSERTAR LOS DATOS A LA TABLA---------------"
def insert_data():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()                          #aqui se obtiene cada elemento de los labels
    estado = combo_asignatura.get()
    checkbox_value = var.get()

    if not id.isdigit():
        messagebox.showerror("Error", "El ID solo puede contener números")
    elif not name.replace(' ', '').isalpha():
        messagebox.showerror("Error", "El nombre solo puede contener letras")
    elif not age.isdigit():                                                                                    #aqui se realiza las validaciones
        messagebox.showerror("Error", "La edad solo puede contener números")
    elif id == "" or name == "" or age == "" or estado == "":
        messagebox.showerror("Error", "Por favor complete todos los campos")
    else:
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM datos WHERE id=%s OR name=%s", (id, name))
            result = cursor.fetchone()
            if result:                                                                     #aqui se selecciona los datos e igual se realiza la validacion si los datos son iguales
                messagebox.showerror("Error", "El ID o el nombre ya existen en la tabla")
            else:
                cursor.execute("INSERT INTO datos VALUES(%s,%s,%s,%s,%s)", (id, name, age, estado, checkbox_value))
                cursor.execute("commit")

                id_entry.delete(0, 'end')
                name_entry.delete(0, 'end')
                age_entry.delete(0, 'end')
                combo_asignatura.set('')
                var.set(0)
                show_data()
                messagebox.showinfo("Insertar", "Datos insertados correctamente")
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

"-----------------------AQUI HACE QUE LOS DATOS INGRESADOS DE LOS LABELS SE MUESTREN---------------------- "
def show_data():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM datos ORDER BY id ASC")
    rows = cursor.fetchall()

    for i in tree.get_children():
        tree.delete(i)

    for row in rows:
        tree.insert('', 'end', values=row)

"---------------------Aqui permite que seleccionando un reglon de la tabla pueda actualizar---------------------------"
def update_data():
    if not tree.selection():
        messagebox.showerror("Error", "Por favor seleccione un elemento para actualizar")
        return

    selected_item = tree.selection()[0]
    old_id = tree.item(selected_item)['values'][0]

    new_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()                                      #aqui se obtiene los datos de las entradas
    estado = combo_asignatura.get()
    checkbox_value = var.get()

    if not new_id.isdigit():
        messagebox.showerror("Error", "El ID solo puede contener números")
    elif not name.replace(' ', '').isalpha():
        messagebox.showerror("Error", "El nombre solo puede contener letras")                 #aqui se valida
    elif not age.isdigit():
        messagebox.showerror("Error", "La edad solo puede contener números")
    elif new_id == "" or name == "" or age == "":
        messagebox.showerror("Error", "Por favor complete todos los campos")
    else:
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM datos WHERE id=%s", (old_id,))
            result = cursor.fetchone()
            if old_id == new_id:
                messagebox.showinfo("ERROR")        #lo que hace mediante esto es que si ya existe la id recheze la entrada
            else:
                cursor.execute("UPDATE datos SET id=%s, name=%s, age=%s, estado=%s, checkbox_value=%s WHERE id=%s",
                               (new_id, name, age, estado, checkbox_value, old_id))
                cursor.execute("commit")

                id_entry.delete(0, 'end')
                name_entry.delete(0, 'end')
                age_entry.delete(0, 'end')
                combo_asignatura.set('')
                var.set(0)
                show_data()
                messagebox.showinfo("Actualizar","Datos actualizados correctamente")
                connection.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))


"---------------------Aqui permite que seleccionando un reglon de la tabla pueda actualizar---------------------------"
def delete_data():
    if not tree.selection():
        messagebox.showerror("Error", "Por favor seleccione un elemento para eliminar")
        return

    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]            #aqui mediante el arreglo 0 es decir la posicion se empieza a seleccionar

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM datos WHERE id=%s", (id,))             #conexion a la base de datos se selecciona los eventos que apartir del id borre los item
        cursor.execute("commit")

        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        combo_asignatura.set('')
        var.set(0)
        show_data()
        messagebox.showinfo("Eliminar", "Datos eliminados correctamente")
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

"--------------------este constructor hace que pueda seleccionar el contenido de las tablas----------------"
def select_item(event):
        if not tree.selection():
            return

        selected_item = tree.selection()[0]
        values = tree.item(selected_item)['values']

        id_entry.delete(0, 'end')
        id_entry.insert(0, values[0])

        name_entry.delete(0, 'end')
        name_entry.insert(0, values[1])

        age_entry.delete(0, 'end')
        age_entry.insert(0, values[2])

        combo_asignatura.set(values[3])

        var.set(values[4])
#aqui empieza el primer frame que son las etiqutas y las entradas
root = tk.Tk()
root.title("CRUD ")
frame1 = tk.Frame(root)
frame1.pack(pady=10)

id_label = tk.Label(frame1, text="ID:")
id_label.grid(row=0, column=0)

id_entry = tk.Entry(frame1)
id_entry.grid(row=0, column=1)

name_label = tk.Label(frame1, text="Nombre:")
name_label.grid(row=1, column=0)

name_entry = tk.Entry(frame1)
name_entry.grid(row=1, column=1)

age_label = tk.Label(frame1, text="Edad:")
age_label.grid(row=2, column=0)

age_entry = tk.Entry(frame1)
age_entry.grid(row=2, column=1)

estado_label = tk.Label(frame1, text="Estado:")
estado_label.grid(row=3, column=0)

combo_asignatura = ttk.Combobox(frame1, state='readonly', values=['Aprobado', 'Reprobado'])
combo_asignatura.grid(row=3, column=1)

var = tk.IntVar()
age_label = tk.Label(frame1, text="Grado:")
age_label.grid(row=4, column=0)
check_1 = tk.Checkbutton(frame1, text='1', variable=var, onvalue=1)
check_2 = tk.Checkbutton(frame1, text='2', variable=var, onvalue=2)
check_3 = tk.Checkbutton(frame1, text='3', variable=var, onvalue=3)

check_1.grid(row=4, column=1)
check_2.grid(row=4, column=2)
check_3.grid(row=4, column=3)
#aqui se empieza el frame 2 donde es el area de los botones
frame2 = tk.Frame(root)
frame2.pack(pady=10)

insert_button = tk.Button(frame2, text="Insertar", command=insert_data)
insert_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(frame2, text="Actualizar", command=update_data)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(frame2, text="Eliminar", command=delete_data)
delete_button.grid(row=0, column=2, padx=5)
#el frame 3 es el contenido de la tabla
frame3 = tk.Frame(root)
frame3.pack(pady=10)

scrollbar = tk.Scrollbar(frame3)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame3, yscrollcommand=scrollbar.set)
tree.pack()

tree['columns'] = ('ID', 'Nombre', 'Edad', 'Estado', 'Grado')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.W, width=80)
tree.column('Nombre', anchor=tk.W, width=140)
tree.column('Edad', anchor=tk.CENTER, width=80)
tree.column('Estado', anchor=tk.W, width=140)
tree.column('Grado', anchor=tk.CENTER, width=80)

tree.heading('#0', text='', anchor=tk.W)
tree.heading('ID', text='ID', anchor=tk.W)
tree.heading('Nombre', text='Nombre', anchor=tk.W)
tree.heading('Edad', text='Edad', anchor=tk.CENTER)
tree.heading('Estado', text='Estado', anchor=tk.W)
tree.heading('Grado', text='Grado', anchor=tk.CENTER)

scrollbar.config(command=tree.yview)

tree.bind('<ButtonRelease-1>', select_item)

show_data()

root.mainloop()