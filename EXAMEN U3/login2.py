import sys
from subprocess import call
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

class Register:
    def __init__(self,v2):
        self.window = v2
        self.window.title("REGISTRO")
        self.window.geometry("680x600")
        self.window.config(bd=10, bg="azure")
        self.window.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico")

        self.titulo = Label(v2, text="REGISTRO", fg="black", bg="azure", font=("Arial", 25, "bold"),pady=5).pack()

        imagen_registro = Image.open(r"c:/pythonProject/EXAMEN U3/FORMULARIOIMG.png")
        nueva_imagen = imagen_registro.resize((200, 200))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.window, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=10, padx=0, ipadx=0)

        # CREACION DEL MARCO PARA EL FORMULARIO
        marco = LabelFrame(v2, text="DATOS PERSONALES", bg="azure", font=("Comic Sans", 15, "bold"))
        marco.config(bd=5, pady=10)
        marco.pack()

        self.matricula_label = tk.Label(marco, text="MSTRÍCULA:",bg="azure", font=("Arial", 12, "bold"))
        self.matricula_label.grid(row=1, column=1, padx=5, pady=8)
        vcmd = (self.window.register(self.validate_matricula), '%P')
        self.matricula_entry = tk.Entry(marco, validate="key", validatecommand=vcmd, font=("Arial", 12))
        self.matricula_entry.grid(row=1, column=2, padx=5, pady=8)

        self.password_label = tk.Label(marco, text="CONTRASEÑA:",bg="azure", font=("Arial", 12, "bold"))
        self.password_label.grid(row=2, column=1, padx=5, pady=8)
        vcmd2 = (self.window.register(self.validate_password), '%P')
        self.password_entry = tk.Entry(marco, show="*", validate="key", validatecommand=vcmd2,font=("Arial", 12))
        self.password_entry.grid(row=2, column=2, padx=5, pady=8)

        self.repeat_password_label = tk.Label(marco, text="REPETIR CONTRASEÑA:",bg="azure", font=("Arial", 12, "bold"))
        self.repeat_password_label.grid(row=3, column=1, padx=5, pady=8)
        vcmd3 = (self.window.register(self.validate_password), '%P')
        self.repeat_password_entry = tk.Entry(marco, show="*", validate="key", validatecommand=vcmd3, font=("Arial", 12))
        self.repeat_password_entry.grid(row=3, column=2, padx=5, pady=8)

        frame_botones = Frame(v2)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        self.register_button = tk.Button(frame_botones, text="REGISTRARSE", command=self.register_user, height=2,width=15,bg="springgreen4",fg="white",font=("Arial",12,"bold"))
        self.register_button.grid(row=4, column=1, padx=5, pady=8)

        self.back_button = tk.Button(frame_botones, text="REGRESAR", command=self.back, height=2,width=15,bg="springgreen4",fg="white",font=("Arial",12,"bold"))
        self.back_button.grid(row=4, column=2, padx=5, pady=8)

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

    def register_user(self):
        matricula = self.matricula_entry.get()
        password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()

        if not matricula or not password or not repeat_password:
            messagebox.showerror("ERROR", "NO DEJES CAMPOS VACIOS")
            return

        if password != repeat_password:
            messagebox.showerror("ERROR", "LAS CONTRASEÑAS NO COINCIEDEN")
            return

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='p4')

        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        result = cursor.fetchone()

        if result:
            # El usuario ya existe
            # Mostrar un mensaje de error o tomar otra acción
            messagebox.showerror("Error", "El usuario ya existe")
        else:
            # El usuario no existe
            # Continuar con el registro del nuevo usuario
            query = "INSERT INTO users (matricula, password) VALUES (%s, %s)"

            try:
                cursor.execute(query, (matricula, password))
                conn.commit()
                messagebox.showinfo("ÉXITO", "USUARIO REGISTRADO CORRECTAMENTE")

                self.window.destroy()
                call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    def back(self):
        self.window.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])



if __name__ == "__main__":
    v2= Tk()
    application = Register(v2)
    v2.mainloop()