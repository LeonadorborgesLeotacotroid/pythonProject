#------FORMULARIO QUE ACOMPAÑE AL LOGIN------------
import sys
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
#PIL ES UNA LIBRERIA QUE PERMITE INSERTAR IMAGENES
from subprocess import call

import sqlite3

class Login_Principal:
    db_name='database_proyecto.db'

#CREAMOS LA VENTANA
    def __init__(self, ventanalogin):
        self.ventana=ventanalogin
        self.ventana.title("LOGIN")
        self.ventana.geometry("630x630")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=10, bg="azure")
        self.ventana.iconbitmap(r"c:/pythonProject/EXAMEN UNIDAD 2/icono.ico")

        titulo=Label(ventanalogin, text="BIENVENIDO GUERRERO",fg="black", bg="azure", font=("Arial", 25, "bold"),pady=5).pack()

       #INSERTAR IMAGEN
        imagen_registro = Image.open("c:/pythonProject/EXAMEN UNIDAD 2/FORMULARIOIMG.png")
        nueva_imagen = imagen_registro.resize((200, 200))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventanalogin, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=10, padx=0, ipadx=0)

       #CREACION DEL MARCO PARA EL FORMULARIO
        marco = LabelFrame(ventanalogin, text="INICIA SESIÓN", bg="azure", font=("Comic Sans", 15, "bold"))
        marco.config(bd=5, pady=10)
        marco.pack()

        #ESTA PARTE SON LOS LABEL CON LA OPCION QUE EL USUARIO INGRESE LOS DATOS matricula, nombre, apellidos,carrera, contraseña,
        label_matricula= Label(marco,text="MATRÍCULA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky='s', padx=6, pady=8)
        self.matricula=Entry(marco,width=20, font=("Arial", 12))
        self.matricula.focus()
        self.matricula.grid(row=0, column=1,padx=6,pady=8)

        label_contrasena= Label(marco, text="CONTRASEÑA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky='s', padx=12, pady=8)
        self.contrasena = Entry(marco, width=20, show="★", font=("Arial", 12))
        self.contrasena.grid(row=1, column=1, padx=12, pady=8)


        #CREACION DE BOTONES
        frame_botones=Frame(ventanalogin)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        boton_registrar=Button(frame_botones,text="INICIAR", command=self.login,height=2,width=10,bg="springgreen4",fg="white",font=("Arial",12,"bold")).grid(row=0, column=1,padx=10, pady=15)
        boton_limpiar = Button(frame_botones, text="REGISTRAR", command=self.Llamar_formulario, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10,pady=15)


    def validar_login(self,matricula,contrasena):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            sql = f"SELECT * FROM REGISTRO WHERE matricula = {matricula} AND contraseña = '{contrasena}'"
            cursor.execute(sql)
            validacion = cursor.fetchall()  # obtener respuesta como lista
            cursor.close()
            return validacion

    def validar_formulariofull(self):
        if len(self.matricula.get()) !=0 and len(self.contrasena.get()) !=0:
            return True
        else:
            messagebox.showerror("ERROR", "POR FAVOR INGRESE LOS DATOS CORRESPONDIENTES")

    def login(self):
        if(self.validar_formulariofull()):
            matricula=self.matricula.get()
            contrasena=self.contrasena.get()
            datos=self.validar_login(matricula,contrasena)
            if(datos != []):
                ventanalogin.destroy()
                call([sys.executable, 'c:/pythonProject/EXAMEN UNIDAD 2/MENU DESPEGABLE.py'])
            else:
                messagebox.showerror("ERROR", "ERROR DE MATRÍCULA Y/O CONTRASEÑA")

    def Llamar_formulario(self):
        ventanalogin.destroy()
        call([sys.executable,'c:/pythonProject/EXAMEN UNIDAD 2/FORMULARIO PARA LOGIN.py'])

if __name__ == '__main__':
  ventanalogin = Tk()
  application = Login_Principal(ventanalogin)
  ventanalogin.mainloop()
