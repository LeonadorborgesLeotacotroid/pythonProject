import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import sys
from subprocess import call

class MyApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("ERROR")
        self.ventana.geometry('500x500')
        self.ventana.config(bg="azure")
        self.ventana.iconbitmap(r"c:/pythonProject/EXAMEN U3/agen.ico")

        img = Image.open(r"c:/pythonProject/EXAMEN U3/pollo1.jpg")
        new_img = img.resize((300, 250))
        render = ImageTk.PhotoImage(new_img)
        img1 = Label(self.ventana, image=render)
        img1.image = render
        img1.place(x=100, y=108)

        espacio = Label(self.ventana, text=" ", bg="azure", font=("Arial", 12), fg="gray1")
        espacio.config(pady="15")
        espacio.pack()
        miEtiqueta1 = Label(self.ventana, text="¡ALGO ESTA MAL, INTENTALO DE NUEVO!", bg="azure", font=("Arial", 12), fg="gray1")
        miEtiqueta1.config(pady="10")
        miEtiqueta1.pack()

        boton = tk.Button(self.ventana, command=self.login, text='ACEPTAR', bg="red", fg="white", font=("Arial", 12, "bold"), height=2, width=10)
        boton.place(x="200", y="400")

    def login(self):
        self.ventana.destroy()
        call([sys.executable, 'c:/pythonProject/EXAMEN U3/login.py'])
        pass

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()