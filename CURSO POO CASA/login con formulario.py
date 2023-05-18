import tkinter as tk
from tkinter import messagebox
import mysql.connector

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")

        # Connect to the database
        self.db = mysql.connector.connect( host="localhost",
            user="root",
            password="",
            database="test"
        )

        self.cursor = self.db.cursor()

        # Create the users table if it doesn't already exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                gender ENUM('Male', 'Female') NOT NULL
            )
        """)

        # Create the form fields
        self.label_username = tk.Label(self.root, text="Username")
        self.label_username.pack()

        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        self.label_password = tk.Label(self.root, text="Password")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.label_last_name = tk.Label(self.root, text="Last Name")
        self.label_last_name.pack()

        self.entry_last_name = tk.Entry(self.root)
        self.entry_last_name.pack()

        self.label_age = tk.Label(self.root, text="Age")
        self.label_age.pack()

        self.entry_age = tk.Entry(self.root)
        self.entry_age.pack()

        self.label_gender = tk.Label(self.root, text="Gender")
        self.label_gender.pack()

        self.var_gender = tk.StringVar(value="Male")
        self.radio_gender_male = tk.Radiobutton(self.root, text="Male", variable=self.var_gender, value="Male")
        self.radio_gender_male.pack()

        self.radio_gender_female = tk.Radiobutton(self.root, text="Female", variable=self.var_gender, value="Female")
        self.radio_gender_female.pack()

        # Create the login and register buttons
        self.button_login = tk.Button(self.root, text="Login", command=self.login)
        self.button_login.pack()

        self.button_register = tk.Button(self.root, text="Register", command=self.register)
        self.button_register.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Query the database to check if the user exists
        self.cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful")

        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        last_name = self.entry_last_name.get()
        age = self.entry_age.get()
        gender = self.var_gender.get()

        # Basic validation for empty fields
        if username == "" or password == "" or last_name == "" or age == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Validate that the username only contains letters
        if not username.isalpha():
            messagebox.showerror("Error", "Username must only contain letters")
            return

        # Validate that the password only contains numbers
        if not password.isdigit():
            messagebox.showerror("Error", "Password must only contain numbers")
            return

        # Validate that the age is a valid integer
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid integer")
            return

        # Insert the new user into the database
        self.cursor.execute(
            "INSERT INTO users (username, password, last_name, age, gender) VALUES (%s, %s, %s, %s, %s)",
            (username, password, last_name, age, gender)
        )
        self.db.commit()

        # Clear the form fields
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)

        messagebox.showinfo("Success", "User registered successfully")

    # Create the main window
root = tk.Tk()

    # Create an instance of the LoginForm class
login_form = LoginForm(root)

root.mainloop()