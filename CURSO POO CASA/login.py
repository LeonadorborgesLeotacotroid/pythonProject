import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Login:
    def __init__(self):
        self.create_database()
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("300x150")

        self.matricula_label = tk.Label(self.window, text="Matricula:")
        self.matricula_label.pack()
        vcmd = (self.window.register(self.validate_matricula), '%P')
        self.matricula_entry = tk.Entry(self.window, validate="key", validatecommand=vcmd)
        self.matricula_entry.pack()

        self.password_label = tk.Label(self.window, text="Contraseña:")
        self.password_label.pack()
        vcmd2 = (self.window.register(self.validate_password), '%P')
        self.password_entry = tk.Entry(self.window, show="*", validate="key", validatecommand=vcmd2)
        self.password_entry.pack()

        self.login_button = tk.Button(self.window, text="Iniciar sesión", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.window, text="Registrarse", command=self.register)
        self.register_button.pack()

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
            messagebox.showerror("Error", "No debe dejar campos vacíos")
            return

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='p4')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE matricula=%s AND password=%s"
        cursor.execute(query, (matricula, password))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Éxito", "Inicio de sesión correcto")
            self.window.destroy()
            SecondWindow()

        else:
            messagebox.showerror("Error", "Matrícula o contraseña incorrectas")

    def register(self):
        self.window.destroy()
        Register()

class Register:
        def __init__(self):
            self.window = tk.Tk()
            self.window.title("Registro")
            self.window.geometry("300x200")

            self.matricula_label = tk.Label(self.window, text="Matricula:")
            self.matricula_label.pack()
            vcmd = (self.window.register(self.validate_matricula), '%P')
            self.matricula_entry = tk.Entry(self.window, validate="key", validatecommand=vcmd)
            self.matricula_entry.pack()

            self.password_label = tk.Label(self.window, text="Contraseña:")
            self.password_label.pack()
            vcmd2 = (self.window.register(self.validate_password), '%P')
            self.password_entry = tk.Entry(self.window, show="*", validate="key", validatecommand=vcmd2)
            self.password_entry.pack()

            self.repeat_password_label = tk.Label(self.window, text="Repetir contraseña:")
            self.repeat_password_label.pack()
            vcmd3 = (self.window.register(self.validate_password), '%P')
            self.repeat_password_entry = tk.Entry(self.window, show="*", validate="key", validatecommand=vcmd3)
            self.repeat_password_entry.pack()

            self.register_button = tk.Button(self.window, text="Registrarse", command=self.register_user)
            self.register_button.pack()

            self.back_button = tk.Button(self.window, text="Regresar", command=self.back)
            self.back_button.pack()

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
                    messagebox.showerror("Error", "No debe dejar campos vacíos")
                    return

                if password != repeat_password:
                    messagebox.showerror("Error", "Las contraseñas no coinciden")
                    return

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='p4')

                cursor = conn.cursor()

                query = "INSERT INTO users (matricula, password) VALUES (%s, %s)"

                try:
                    cursor.execute(query, (matricula, password))
                    conn.commit()
                    messagebox.showinfo("Éxito", "Usuario registrado correctamente")

                    self.window.destroy()
                    Login()

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error: {err}")

        def back(self):
                self.window.destroy()
                Login()

class SecondWindow:
    def __init__(self):
            self.window = tk.Tk()
            self.window.title("Ventana 2")

if __name__ == "__main__":
        login = Login()
        login.window.mainloop()
