import sys
from subprocess import call
from tkinter import *
from PIL import ImageTk, Image
#PIL ES UNA LIBRERIA QUE PERMITE INSERTAR IMAGENES


class HORARIO:

#CREAMOS LA VENTANA
    def __init__(self,ventanahorario):
        self.ventana=ventanahorario
        self.ventana.title("HORARIO")
        self.ventana.geometry("650x600")
        self.ventana.resizable(0,0)
        self.ventana.config(bd=10, bg="azure")
        self.ventana.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico")

        titulo = Label(ventanahorario, bg="azure", fg="black", font=("Arial", 20, "bold"), pady=2).pack()

        #INSERTAR IMAGEN
        imagen_registro = Image.open("c:/pythonProject/EXAMEN U3/HORARIO.jpg")
        nueva_imagen = imagen_registro.resize((600, 424))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventanahorario, image=render)
        label_imagen.image = render
        label_imagen.config(bg="azure")
        label_imagen.pack(pady=0,padx=0)

        #Botones
        frame_botones = Frame(ventanahorario)
        frame_botones.config(bg="azure")
        frame_botones.pack()

        boton_menu = Button(frame_botones, text="MENÚ PRINCIPAL", command=self.llamar_menu, height=2, width=15,bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10,pady=15)
        boton_eliminar = Button(frame_botones, text="SALIR", command=self.llamar_login, height=2, width=10, bg="springgreen4", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10, pady=15)

    def llamar_login(self):
        ventanahorario.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])
        #

    def llamar_menu(self):
        ventanahorario.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/MENU DESPEGABLE.py'])


if __name__ == '__main__':
  ventanahorario = Tk()
  application = HORARIO(ventanahorario)
  ventanahorario.mainloop()

