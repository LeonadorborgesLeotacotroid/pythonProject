import sys
from subprocess import call
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

class Login:

    def __init__(self,v1):
        self.create_database()
        self.window = v1
        self.window.title("LOGIN")
        self.window.geometry("680x600")
        self.window.config(bd=10, bg="azure")
        self.window.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico" )

        self.titulo = Label(v1, text="BIENVENIDO GUERRERO", fg="black", bg="azure", font=("Arial", 25, "bold"),pady=5).pack()

        # INSERTAR IMAGEN
        imagen_registro = Image.open(r"c:/pythonProject/EXAMEN U3/FORMULARIOIMG.png")
        nueva_imagen = imagen_registro.resize((200, 200))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.window, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=10, padx=0, ipadx=0)

        # CREACION DEL MARCO PARA EL FORMULARIO
        marco = LabelFrame(v1, text="INICIA SESIÓN", bg="azure",font=("Comic Sans", 15, "bold"))
        marco.config(bd=5, pady=10)
        marco.pack()

        self.matricula_label = tk.Label(marco, text="MATRÍCULA:",bg="azure", font=("Arial", 12, "bold"))
        self.matricula_label.grid(row=1, column=1, padx=5, pady=8)
        vcmd = (marco.register(self.validate_matricula), '%P')
        self.matricula_entry = tk.Entry(marco, validate="key", validatecommand=vcmd,width=20, font=("Arial", 12))
        self.matricula_entry.grid(row=1, column=2, padx=5, pady=8)

        self.password_label = tk.Label(marco, text="CONTRASEÑA:", bg="azure", font=("Arial", 12, "bold"))
        self.password_label.grid(row=2, column=1, padx=5, pady=8)
        vcmd2 = (marco.register(self.validate_password), '%P')
        self.password_entry = tk.Entry(marco, show="★", validate="key", validatecommand=vcmd2, width=20, font=("Arial", 12))
        self.password_entry.grid(row=2, column=2, padx=5, pady=8)

        frame_botones = Frame(v1)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        self.login_button = tk.Button(frame_botones , text="INICIAR SESIÓN", command=self.login, height=2,width=15,bg="springgreen4",fg="white",font=("Arial",12,"bold"))
        self.login_button.grid(row=3, column=1, padx=5, pady=8)

        self.register_button = tk.Button(frame_botones , text="REGISTRARSE", command=self.register, height=2, width=15,bg="springgreen4", fg="white", font=("Arial", 12, "bold"))
        self.register_button.grid(row=3, column=2, padx=5, pady=8)

    def create_database(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS p4")
        cursor.execute("USE p4")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,matricula VARCHAR(8) NOT NULL,password VARCHAR(8) NOT NULL)")
        conn.commit()
        cursor.close()
        conn.close()

    def validate_matricula(self, new_text):
        if not new_text:
            return True
        try:
            if int(new_text) >= 0 and len(new_text) <= 8:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_password(self, new_text):
        if not new_text:
            return True
        if len(new_text) <= 8:
            return True
        else:
            return False

    def login(self):
        matricula = self.matricula_entry.get()
        password = self.password_entry.get()

        if not matricula or not password:
            self.window.destroy()
            call([sys.executable, 'c:/pythonProject/EXAMEN U3/pollo1.py'])

            return

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='p4')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE matricula=%s AND password=%s"
        cursor.execute(query, (matricula, password))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("ÉXITO", "INICIO DE SESIÓN CORRECTO")
            self.window.destroy()
            call([sys.executable, 'c:/pythonProject/EXAMEN U3/MENU DESPEGABLE.py'])

        else:
            self.window.destroy()
            call([sys.executable, 'c:/pythonProject/EXAMEN U3/pollo1.py'])

    def register(self):
        self.window.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login2.py' ])


if __name__ == "__main__":
    v1= Tk()
    application = Login(v1)
    v1.mainloop()

