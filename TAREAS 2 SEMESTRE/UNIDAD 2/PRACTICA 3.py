#Leonardo Borges LOGIN CON BASE DE DATOS
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# crear tabla base de datos
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()


# se crea clase main
class main:
    def __init__(self, master):
        # VENTANA
        self.master = master
        # variables a stringvar
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # aqui llaman a los widgets
        self.widgets()

    # Login
    def login(self):
        # conexion con la base de datos
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # encontrar usuarios
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Estas registrado' #si el usuario es correcto abrira una ventana con su nombre
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Usuario no encontrado.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # apartado para saber si al momento de crear un nuevo usuario existe o no
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])

        if c.fetchall():
            ms.showerror('Error!', 'Intente otro usuario.')
        else:
            ms.showinfo('Felicidades usuario creado :3')
            self.log()
        # Creacion del nuevo usuario
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


        #PARTES DEL FRAMEWORK

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Crear cuenta'
        self.crf.pack()

    # Labeñs
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Usuario: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Contraseña: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Crear cuenta ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Usuario: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Contraseña: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Crear cuenta', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Registrate ahora', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,column=1)


if __name__ == '__main__':

    root = Tk()
    root.title('Login leotaco')
    main(root)
    root.mainloop()