import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector


def create_database():
    conn = mysql.connector.connect(user='root', password='', host='localhost')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS p3")
    cursor.execute("USE p3")
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT PRIMARY KEY, value INT, date DATE, task VARCHAR(255))")
    conn.commit()
    cursor.close()
    conn.close()


def validate_id(id_entry):
    if len(id_entry.get()) > 3:
        id_entry.delete(3)
    if not id_entry.get().isdigit():
        id_entry.delete(0, tk.END)


def validate_value(value_entry):
    if len(value_entry.get()) > 3:
        value_entry.delete(3)
    if not value_entry.get().isdigit():
        value_entry.delete(0, tk.END)


def add_task(id_entry, value_entry, date_entry, task_combobox, treeview):
    id = id_entry.get()
    value = value_entry.get()
    date = date_entry.get()
    task = task_combobox.get()

    if not id:
        tk.messagebox.showerror("Error", "ID cannot be empty")
        return

    if not value:
        tk.messagebox.showerror("Error", "Value cannot be empty")
        return

    # Connect to database and check if data already exists
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='p3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    data = cursor.fetchall()
    if data:
        tk.messagebox.showerror("Error", "ID already exists")
        return



    # Insert data
    cursor.execute("INSERT INTO tasks (id, value, date, task) VALUES (%s, %s, %s, %s)", (id, value, date, task))
    conn.commit()
    cursor.close()
    conn.close()

    # Update treeview
    treeview.insert('', 'end', values=(id, value, date, task))



def delete_task(treeview):
    if not treeview.selection():
        tk.messagebox.showerror("Error", "Please select an item to delete")
        return

    selected_item = treeview.selection()[0]
    id = treeview.item(selected_item)['values'][0]

    # Connect to database and delete data
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='p3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    # Update treeview
    treeview.delete(selected_item)

def update_task(id_entry, value_entry, date_entry, task_combobox, treeview):
    if not treeview.selection():
        tk.messagebox.showerror("Error", "Please select an item to update")
        return


    selected_item = treeview.selection()[0]
    id = id_entry.get()
    value = value_entry.get()
    date = date_entry.get()
    task = task_combobox.get()

    # Connect to database and check if data already exists
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='p3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=%s AND id!=%s", (id, treeview.item(selected_item)['values'][0]))
    data = cursor.fetchall()


    if data:
        tk.messagebox.showerror("Error", "ID already exists")
        return



    # Update data
    cursor.execute("UPDATE tasks SET value=%s, date=%s, task=%s WHERE id=%s", (value, date, task, id))
    conn.commit()
    cursor.close()
    conn.close()

    # Update treeview
    treeview.item(selected_item, values=(id, value, date, task))



def search_task(id_entry, treeview):
    id = id_entry.get()

    # Connect to database and get data
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='p3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=%s ORDER BY date ASC", (id,))
    data = cursor.fetchall()

    # Update treeview
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert('', 'end', values=row)

    cursor.close()
    conn.close()


def show_all(treeview):
    # Connect to database and get data
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='p3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY date ASC")
    data = cursor.fetchall()

    # Update treeview
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert('', 'end', values=row)

    cursor.close()
    conn.close()


create_database()

root = tk.Tk()

id_label = tk.Label(root, text="ID:")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

value_label = tk.Label(root, text="Value:")
value_label.pack()

value_entry = tk.Entry(root)
value_entry.pack()

date_label = tk.Label(root, text="Date:")
date_label.pack()

date_entry = DateEntry(root)
date_entry.pack()

task_label = tk.Label(root, text="Task:")
task_label.pack()

task_combobox = ttk.Combobox(root)
task_combobox['values'] = ('Task 1', 'Task 2')
task_combobox.current(0)
task_combobox.pack()

treeview = ttk.Treeview(root)
treeview['columns'] = ('ID', 'Value', 'Date', 'Task')
treeview.heading('ID', text='ID')
treeview.heading('Value', text='Value')
treeview.heading('Date', text='Date')
treeview.heading('Task', text='Task')
treeview.pack()

add_button = tk.Button(root, text="Add",
                       command=lambda: add_task(id_entry, value_entry, date_entry, task_combobox, treeview))
add_button.pack()

delete_button = tk.Button(root, text="Delete", command=lambda: delete_task(treeview))
delete_button.pack()

update_button = tk.Button(root, text="Update",
                          command=lambda: update_task(id_entry, value_entry, date_entry, task_combobox, treeview))
update_button.pack()

search_button = tk.Button(root, text="Search", command=lambda: search_task(id_entry, treeview))
search_button.pack()

show_all_button = tk.Button(root, text="Show All", command=lambda: show_all(treeview))
show_all_button.pack()

id_entry.bind('<KeyRelease>', lambda e: validate_id(id_entry))
value_entry.bind('<KeyRelease>', lambda e: validate_value(value_entry))

root.mainloop()
