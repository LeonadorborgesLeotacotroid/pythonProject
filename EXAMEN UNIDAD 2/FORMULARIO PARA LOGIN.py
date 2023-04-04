import sys
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
#PIL ES UNA LIBRERIA QUE PERMITE INSERTAR IMAGENES
from subprocess import call
import sqlite3

class Registro:
    db_name='database_proyecto.db'
#CREAMOS LA VENTANA
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("REGISTRO")
        self.ventana.geometry("550x630")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=10, bg="azure")
        self.ventana.iconbitmap(r"C:/pythonProject/EXAMEN UNIDAD 2\icono.ico")

        titulo=Label(ventana, text="REGISTRO",fg="black", bg="azure" ,font=("Arial", 20,"bold"),pady=0).pack()

       #INSERTAR IMAGEN
        imagen_registro = Image.open("c:/pythonProject/EXAMEN UNIDAD 2/FORMULARIOIMG.png")
        nueva_imagen = imagen_registro.resize((150, 150))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventana, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=2)

       #CREACION DEL MARCO PARA EL FORMULARIO
        marco = LabelFrame(ventana, text="Datos personales", bg="azure", font=("Comic Sans", 15, "bold"))
        marco.config(bd=5, pady=10)
        marco.pack()

        #ESTA PARTE SON LOS LABEL CON LA OPCION QUE EL USUARIO INGRESE LOS DATOS matricula, nombre, apellidos,carrera, contraseña,
        label_matricula= Label(marco,text="MATRÍCULA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=0, column=0,sticky='s', padx=6, pady=8)
        self.matricula=Entry(marco,width=20, font=("Arial", 12))
        self.matricula.focus()
        self.matricula.grid(row=0, column=1,padx=6,pady=8)

        label_nombres = Label(marco, text="NOMBRES: ", bg="azure", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky='s',padx=12, pady=8)
        self.nombres = Entry(marco, width=20, font=("Arial", 12))
        self.nombres.grid(row=1, column=1, padx=12, pady=8)

        label_apellidos = Label(marco, text="APELLIDOS: ", bg="azure", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky='s',padx=12, pady=8)
        self.apellidos = Entry(marco, width=20, font=("Arial", 12))
        self.apellidos.grid(row=2, column=1, padx=12, pady=8)

        label_carrera = Label(marco, text="CARRERA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky='s',padx=12, pady=8)
        self.combo_carrera=ttk.Combobox(marco,values=["SISTEMAS","RENOVABLES","ELECTROMECÁNICA","LOGÍSTICA","ADMINISTRACIÓN"],width=22,state="readonly", font=("Arial", 12))
        self.combo_carrera.current(0)

        self.combo_carrera.grid(row=3, column=1, padx=12, pady=8)

        label_contrasena= Label(marco, text="CONTRASEÑA: ", bg="azure", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky='s', padx=12, pady=8)
        self.contrasena = Entry(marco, width=20, show="✦", font=("Arial", 12))
        self.contrasena.grid(row=4, column=1, padx=12, pady=8)

        label_contrasena = Label(marco, text=" REPETIR CONTRASEÑA: ",bg="azure", font=("Arial", 12, "bold")).grid(row=5, column=0,sticky='s', padx=12,pady=8)
        self.repetir_contrasena = Entry(marco, width=20, show="✦",font=("Arial", 12))
        self.repetir_contrasena.grid(row=5, column=1, padx=12, pady=8)

        #CREACION DE BOTONES
        frame_botones=Frame(ventana)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        boton_registrar=Button(frame_botones,text="REGISTRAR", command=self.Registrar_usuario,height=2,width=10,bg="springgreen4",fg="white",font=("Arial",12,"bold")).grid(row=0, column=1,padx=10, pady=15)
        boton_limpiar = Button(frame_botones, text="LIMPIAR", command=self.Limpiar_formulario, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="REGRESAR", command=self.Llamar_login, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10,pady=15)

    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
        return result

    def validar_formulariofull(self):
        if len(self.matricula.get()) !=0 and len(self.nombres.get()) !=0 and len(self.apellidos.get()) !=0 and len(self.combo_carrera.get()) !=0 and len(self.contrasena.get()) !=0 and len(self.repetir_contrasena.get()) !=0 :
            return True
        else:
            messagebox.showerror("ERROR","COMPLETA LOS DATOS SOLICITADOS")


    def validar_contrasena(self):
        if(str(self.contrasena.get()) == str(self.repetir_contrasena.get())):
            return True
        else:
            messagebox.showerror("ERROR", "CONTRASEÑAS NO COINCIDEN")

    def Buscar_matricula(self, matricula):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            sql="SELECT * FROM REGISTRO WHERE matricula ={}".format(matricula)
            cursor.execute(sql)
            dn=cursor.fetchall()
            cursor.close()
            return dn

    def Validar_matricula(self):
        matricula=self.matricula.get()
        dato=self.Buscar_matricula(matricula)
        if (dato == []):
            return True
        else:
            messagebox.showerror("ERROR", "MATRÍCULA REGISTRADA ANTERIORMENTE")

    def Registrar_usuario(self):
        if self.validar_formulariofull() and self.validar_contrasena() and self.validar_contrasena():
            query = 'INSERT INTO REGISTRO VALUES(NULL, ?,?,?,?,?)'
            parameters = (self.matricula.get(),self.nombres.get(),self.apellidos.get(),self.combo_carrera.get(),self.contrasena.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Bienvenido {self.nombres.get()} {self.apellidos.get()}')
            print('USUARIO CREADO')
            self.Limpiar_formulario()

    def Limpiar_formulario(self):
        self.matricula.delete(0, END)
        self.nombres.delete(0, END)
        self.apellidos.delete(0, END)
        self.combo_carrera.delete(0, END)
        self.contrasena.delete(0, END)
        self.repetir_contrasena.delete(0, END)

    def Llamar_login(self):
        ventana.destroy()
        call([sys.executable,'c:/pythonProject/EXAMEN UNIDAD 2/LOGIN.py'])


if __name__ == '__main__':
    ventana = Tk()
    application = Registro(ventana)
    ventana.mainloop()



