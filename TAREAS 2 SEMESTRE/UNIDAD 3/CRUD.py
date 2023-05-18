from tkinter import *
from tkinter import messagebox
import mysql.connector

# Conectar a la base de datos
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela"
    )
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()


# Crear la tabla de alumnos si no existe
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT, email VARCHAR(255))")

# Función para leer todos los alumnos de la base de datos
def leer_alumnosDB():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos")
    return cursor.fetchall()

# Función para agregar un nuevo alumno a la base de datos
def agregar_alumnoDB(nombre, edad, email):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (%s, %s, %s)", (nombre, edad, email))
        db.commit()
    except mysql.connector.Error as error:
        messagebox.showerror("Error al agregar el alumno", f"No se pudo agregar el alumno: {error}")
    finally:
        cursor.close()


# Función para actualizar un alumno existente en la base de datos
def actualizar_alumnoDB(id, nombre, edad, email):
    iid = int(id)
    cursor = db.cursor()
    print("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    cursor.execute("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    db.commit()

# Función para eliminar un alumno existente de la base de datos
def eliminar_alumnoDB(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    db.commit()

# Función para mostrar una lista de todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla
    for widget in tabla_alumnos.winfo_children():
        widget.destroy()

    # Obtener todos los alumnos
    alumnos = leer_alumnosDB()

    # Mostrar los alumnos en la tabla
    for i, alumno in enumerate(alumnos):
        id = alumno[0]
        nombre = alumno[1]
        edad = alumno[2]
        email = alumno[3]

        Label(tabla_alumnos, text=id).grid(row=i, column=0)
        Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
        Label(tabla_alumnos, text=edad).grid(row=i, column=2)
        Label(tabla_alumnos, text=email).grid(row=i, column=3)

# Función para agregar un nuevo alumno
def agregar_alumno():
    # Obtener los datos del nuevo alumno
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()

    # Validar que los campos no estén vacíos
    if not nombre or not edad or not email:
        messagebox.showerror("Error al agregar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Agregar el nuevo alumno
    agregar_alumnoDB(nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()

# Función para actualizar un alumno existente
def actualizar_alumno():
    # Obtener los datos del alumno a actualizar
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()
    id = entrada_id.get()

    # Validar que los campos no estén vacíos
    if not id or not nombre or not edad or not email:
        messagebox.showerror("Error al actualizar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Actualizar el alumno
    actualizar_alumnoDB(id, nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_id.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()


# Función para eliminar un alumno existente
def eliminar_alumno():
    # Obtener el ID del alumno a eliminar
    id = entrada_id.get()

    # Validar que se haya ingresado un ID
    if not id:
        messagebox.showerror("Error al eliminar el alumno", "Por favor ingrese el ID del alumno a eliminar")
        return

    # Preguntar al usuario si está seguro de eliminar el alumno
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este alumno?")

    if confirmar:
        # Eliminar el alumno
        eliminar_alumnoDB(id)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()


# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo CRUD con Python y MySQL")

# Crear los campos de entrada para los datos del alumno
Label(ventana, text="Id:").grid(row=0, column=0, padx=5, pady=5)
entrada_id = Entry(ventana)
entrada_id.grid(row=0, column=1, padx=5, pady=5)

Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
entrada_nombre = Entry(ventana)
entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
entrada_edad = Entry(ventana)
entrada_edad.grid(row=2, column=1, padx=5, pady=5)

Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5)
entrada_email = Entry(ventana)
entrada_email.grid(row=3, column=1, padx=5, pady=5)

# Crear los botones para agregar, actualizar y eliminar alumnos
Button(ventana, text="Agregar alumno", command=agregar_alumno).grid(row=0, column=2, padx=5, pady=5)
Button(ventana, text="Actualizar alumno", command=actualizar_alumno).grid(row=1, column=2, padx=5, pady=5)
Button(ventana, text="Eliminar alumno", command=eliminar_alumno).grid(row=2, column=2, padx=5, pady=5)

# Crear la tabla para mostrar los alumnos
tabla_alumnos = Frame(ventana)
tabla_alumnos.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

Label(tabla_alumnos, text="ID").grid(row=0, column=0)
Label(tabla_alumnos, text="Nombre").grid(row=0, column=1)
Label(tabla_alumnos, text="Edad").grid(row=0, column=2)
Label(tabla_alumnos, text="Email").grid(row=0, column=3)

# Mostrar la lista de alumnos en la tabla
mostrar_alumnos()

# Iniciar el loop de la ventana
ventana.mainloop()