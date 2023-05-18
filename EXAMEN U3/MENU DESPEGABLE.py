import tkinter as tk
import sys
from PIL import ImageTk, Image
from subprocess import call

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("MENÚ PRINCIPAL")
        self.master.geometry("530x600")
        self.master.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico")

        # Establecer tamaño mínimo de la ventana
        master.minsize(0,0)

        # Crear el marco principal
        self.marco_principal = tk.Frame(master)
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        # Crear el marco del menú lateral
        self.marco_menu = tk.Frame(self.marco_principal, width=100, bg="azure")
        self.marco_menu.pack(side=tk.LEFT, fill=tk.Y)

        # Crear los botones del menú lateral
        self.boton1 = tk.Button(self.marco_menu, text="HORARIO", bg="springgreen4", fg="white",font=("Arial",10,"bold"), command=self.llamar_horario)
        self.boton1.pack(pady=30, padx=20)
        self.boton2 = tk.Button(self.marco_menu, text="CALENDARIO", bg="springgreen4", fg="white",font=("Arial",10,"bold"), command=self.llamar_calendario)
        self.boton2.pack(pady=30, padx=20)
        self.boton3 = tk.Button(self.marco_menu, text="MIS TAREAS", bg="springgreen4", fg="white",font=("Arial",10,"bold"), command=self.llamar_mistareas)
        self.boton3.pack(pady=30, padx=20)
        self.boton3 = tk.Button(self.marco_menu, text="SALIR", bg="springgreen4", fg="white",font=("Arial",10,"bold"), command=self.llamar_login)
        self.boton3.pack(pady=60, padx=20)

        #Imagen para el menú
        imagen_menu = Image.open("c:/pythonProject/EXAMEN U3/MENU.png")
        nueva_imagen = imagen_menu.resize((100, 100))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = tk.Label(self.marco_menu, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=0, padx=0, ipadx=0)

        # Crear el marco del contenido principal
        self.marco_contenido = tk.Frame(self.marco_principal)
        self.marco_contenido.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear el contenido principal
        self.label_contenido = tk.Label(self.marco_contenido, text="Contenido principal")
        self.label_contenido.pack(pady=0, padx=0)

        # Imagen para el contenido principal
        imagen_contenido = Image.open("c:/pythonProject/EXAMEN UNIDAD 2/FONDO.jpg")
        nueva_imagen = imagen_contenido.resize((530, 600))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = tk.Label(self.label_contenido, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=0, padx=0, ipadx=0)


        # Hacer que el marco del menú lateral sea redimensionable
        self.marco_principal.columnconfigure(0, weight=1)
        self.marco_menu.rowconfigure(0, weight=1)

        # Hacer que la ventana sea redimensionable
        self.marco_principal.columnconfigure(1, weight=1)
        self.marco_principal.rowconfigure(0, weight=1)

    def llamar_login(self):
        root.destroy()
        call([sys.executable,'c:/pythonProject/EXAMEN U3/login.py'])
    def llamar_horario(self):
        root.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/HORARIO.py'])

    def llamar_calendario(self):
        root.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/CALENDARIO.py'])

    def llamar_mistareas(self):
        root.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/crud.py'])


if __name__ == '__main__':
    root = tk.Tk()
    ventana_principal = VentanaPrincipal(root)
    root.mainloop()
