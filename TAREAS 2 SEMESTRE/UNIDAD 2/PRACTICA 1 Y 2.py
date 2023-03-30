import tkinter as tk
from tkinter import *
class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Ejemplo de pantalla con menú")
        self.config(bg="cyan")

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)



        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=20, bg="wheat")
        self.file_menu.add_command(label="Abrir archivo", command=self.open_file)
        self.file_menu.add_command(label="Guardar archivo", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)


        self.edit_menu = tk.Menu(self.menu_bar, tearoff=20)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.label = tk.Label(self, text="¡Hola, mundo!")
        self.label.config(fg="red", bg="cyan", font=("sketch", 20))
        self.label.pack(pady=0)

        self.button = tk.Button(self, text="Presionar", command=self.press_button)
        self.button.config(fg="red", bg="wheat", font=("tahoma", 20))
        self.button.pack(pady=10)

        self.button = tk.Button(self, text="salir", command=ventana.quit)
        self.button.config(fg="red", bg="wheat", font=("tohoma", 20))
        self.button.pack()

        self.pack()

        self.pack()

    def open_file(self): #se muestra en la consola o terminal
        print("Abrir archivo")

    def save_file(self):
        print("Guardar archivo")

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Copiar")

    def paste(self):
        print("Pegar")

    def press_button(self):
        print("Botón presionado")
def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admin" and contrasena == "admin":
        resultado.config(text="Inicio de sesión exitoso")
        root = tk.Tk()
        root.geometry("420x380")
        root.config(bg="cyan")
        app = MenuScreen(root)
        app.mainloop()
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
#ventana.configure(padx=50) #ancho es x
ventana.geometry("480x480")
ventana.config(bg="wheat")

# Crear campos de entrada para el nombre de usuario y la contraseña

nombre_usuario = tk.Entry(ventana)
label = tk.Label( text="Ingresa tu usuario")
label.config(fg="indianred",bg="wheat",font=("tahoma",20))
label.pack(padx=0)

nombre_usuario.pack(pady=20)
contrasena_usuario = tk.Entry(ventana, show="*")
label = tk.Label( text="ingresa tu contraseña")
label.pack(pady=0)
label.config(fg="indianred",bg="wheat",font=("tahoma",20))
label.pack(padx=0)
contrasena_usuario.pack(pady=20)

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=50, pady=50)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()


# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(padx=420)
resultado.pack(pady=380)

ventana.mainloop()