import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Ejemplo")

        self.combo_var = tk.StringVar()
        self.combo = ttk.Combobox(self.master, textvariable=self.combo_var, values=["Opción 1", "Opción 2", "Opción 3"])
        self.combo.grid(row=0, column=0)

        self.date_entry = DateEntry(self.master)
        self.date_entry.grid(row=0, column=1)

        self.calculate_button = tk.Button(self.master, text="Calcular", command=self.calculate)
        self.calculate_button.grid(row=1, column=0)

    def calculate(self):
        if self.combo_var.get() == "Opción 1":
            top = tk.Toplevel(self.master)
            top.title("Ingresar datos")

            tk.Label(top, text="Columna 3:").grid(row=0, column=0)
            entry_3 = tk.Entry(top)
            entry_3.grid(row=0, column=1)

            tk.Label(top, text="Columna 5:").grid(row=1, column=0)
            entry_5 = tk.Entry(top)
            entry_5.grid(row=1, column=1)

            tk.Label(top, text="Columna 6:").grid(row=2, column=0)
            entry_6 = tk.Entry(top)
            entry_6.grid(row=2, column=1)

            calculate_button = tk.Button(top, text="Calcular",
                                         command=lambda: self.calculate_top(entry_3.get(), entry_5.get(),
                                                                            entry_6.get()))
            calculate_button.grid(row=3, column=0)

    def calculate_top(self, value_3, value_5, value_6):
        value_3 = float(value_3)
        value_5 = float(value_5)
        value_6 = float(value_6)

        value_8 = value_3 * value_6
        value_10 = value_8
        value_7 = value_10 / value_5

        result_top = tk.Toplevel(self.master)
        result_top.title("Resultados")

        tk.Label(result_top, text="Columna 1:").grid(row=0, column=0)
        tk.Label(result_top, text=self.date_entry.get()).grid(row=0, column=1)

        tk.Label(result_top, text="Columna 2:").grid(row=1, column=0)
        tk.Label(result_top, text=self.combo_var.get()).grid(row=1, column=1)

        tk.Label(result_top, text="Columna 3:").grid(row=2, column=0)
        tk.Label(result_top, text=value_3).grid(row=2, column=1)

        tk.Label(result_top, text="Columna 4:").grid(row=3, column=0)

        tk.Label(result_top, text="Columna 5:").grid(row=4, column=0)
        tk.Label(result_top, text=value_5).grid(row=4, column=1)

        tk.Label(result_top, text="Columna 6:").grid(row=5, column=0)
        tk.Label(result_top, text=value_6).grid(row=5, column=1)

        tk.Label(result_top, text="Columna 7:").grid(row=6, column=0)
        tk.Label(result_top, text=value_7).grid(row=6, column=1)

        tk.Label(result_top, text="Columna 8:").grid(row=7, column=0)
        tk.Label(result_top, text=value_8).grid(row=7, column=1)



        tk.Label(result_top, text="Columna 9:").grid(row=9, column=0)
        tk.Label(result_top, text=value_10).grid(row=9, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
