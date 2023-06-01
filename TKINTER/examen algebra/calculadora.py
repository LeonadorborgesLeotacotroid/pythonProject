import tkinter as tk

def create_entries(event):
    n = int(entry_n.get())
    for entry in entries:
        entry.destroy()
    entries.clear()
    for i in range(n):
        entry_row = tk.Entry(root)
        entry_row.pack()
        entries.append(entry_row)

def gauss(event):
    n = int(entry_n.get())
    matrix = []
    for i in range(n):
        row = list(map(float, entries[i].get().split()))
        matrix.append(row)
    for i in range(n):
        for j in range(i+1, n):
            ratio = matrix[j][i]/matrix[i][i]
            for k in range(n+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    x = [0 for i in range(n)]
    x[n-1] = matrix[n-1][n]/matrix[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = matrix[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - matrix[i][j]*x[j]
        x[i] = x[i]/matrix[i][i]
    result.set("Result: " + str(x))

root = tk.Tk()
root.title("Gauss Method")

label_n = tk.Label(root, text="Enter the size of the system:")
entry_n = tk.Entry(root)
label_n.pack()
entry_n.pack()

button_create_entries = tk.Button(root, text="Create entries")
button_create_entries.bind("<Button-1>", create_entries)
button_create_entries.pack()

label_matrix = tk.Label(root, text="Enter the coefficients separated by spaces:")
label_matrix.pack()

entries = []

result = tk.StringVar()
result.set("Result: ")
label_result = tk.Label(root, textvariable=result)
label_result.pack()

button_solve = tk.Button(root, text="Solve")
button_solve.bind("<Button-1>", gauss)
button_solve.pack()

root.mainloop()
