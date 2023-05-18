import sys
from subprocess import call
from tkinter import *
from PIL import ImageTk, Image
#PIL ES UNA LIBRERIA QUE PERMITE INSERTAR IMAGENES


class CALENDARIO:

#CREAMOS LA VENTANA SU TAMAÑO
    def __init__(self,ventanacalendario):
        self.ventana=ventanacalendario
        self.ventana.title("CALENDARIO")
        self.ventana.geometry("700x730")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=10, bg="azure")
        self.ventana.iconbitmap(r"C:/pythonProject/EXAMEN U3/agen.ico")

       #ES EL TITULO AQUI
        titulo=Label(ventanacalendario, text="CALENDARIO",fg="black",bg="azure", font=("Arial", 20,"bold"),pady=10).pack()

        #INSERTAR IMAGEN
        imagen_registro = Image.open("c:/pythonProject/EXAMEN U3/CALENDARIO.jpeg") #ACA CAMBIAR HACIA SU DIRRECION
        nueva_imagen = imagen_registro.resize((500, 554))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventanacalendario, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=0,padx=0)

        #ES EL ESPACIO HACIA LOS BOTONES
        frame_botones = Frame(ventanacalendario)
        frame_botones.config(bg="azure")
        frame_botones.pack()
        #SON LOS BOTONES
        boton_eliminar = Button(frame_botones, text="SALIR", command=self.llamar_login, height=2, width=10,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=3,padx=10, pady=5)
        boton_menu = Button(frame_botones, text="MENU PRINCIPAL", command=self.llamar_menu, height=2, width=15,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10,pady=15)


  #FUNCIONES QUE SE UBICAN EN LOS COMANDOS DE LOS BOTONES
    def llamar_login(self):
        ventanacalendario.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])


    def llamar_menu(self):
         ventanacalendario.destroy()
         call([sys.executable, 'c:/pythonProject/EXAMEN U3/MENU DESPEGABLE.py'])
    #

if __name__ == '__main__':
  ventanacalendario= Tk()
  application = CALENDARIO(ventanacalendario)
  ventanacalendario.mainloop()
