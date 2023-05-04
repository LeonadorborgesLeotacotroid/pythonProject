import random
import tkinter as tk

class SeatReservationSystem:

    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.numSeats = numRows * numCols
        self.seats = [[False] * numCols for _ in range(numRows)]
        self.reservedSeats = [-1] * self.numSeats
        self.nextReservationCode = 1

    def reserveSeat(self, row, col):
        if row < 0 or row >= self.numRows or col < 0 or col >= self.numCols:
            self.statusVar.set("Invalid seat selected.")
            return
        if self.seats[row][col]:
            self.statusVar.set("Seat is already reserved.")
            return
        self.seats[row][col] = True
        self.reservedSeats[self.nextReservationCode - 1] = row * self.numCols + col
        self.statusVar.set(f"Seat {chr(row+65)}{col+1} has been reserved.\nYour reservation code is {self.nextReservationCode}")
        self.nextReservationCode += 1
        self.updateSeats()

    def printReservation(self, reservationCode):
        index = reservationCode - 1
        if index < 0 or index >= self.numSeats or self.reservedSeats[index] == -1:
            self.statusVar.set("Invalid reservation code.")
            return
        row = self.reservedSeats[index] // self.numCols
        col = self.reservedSeats[index] % self.numCols
        self.statusVar.set(f"Reservation code: {reservationCode}\nSeat: {chr(row+65)}{col+1}")

    def createSeatButton(self, row, col):
        def seatButtonClick():
            self.reserveSeat(row, col)
        color = "green" if not self.seats[row][col] else "red"
        text = f"{chr(row+65)}{col+1}"
        return tk.Button(self.frameSeats, text=text, bg=color, command=seatButtonClick, width=3, height=1)

    def updateSeats(self):
        for widget in self.frameSeats.winfo_children():
            widget.destroy()
        for i in range(self.numRows):
            for j in range(self.numCols):
                button = self.createSeatButton(i, j)
                button.grid(row=i, column=j)

    def start(self):
        self.root = tk.Tk()
        self.root.title("Seat Reservation System")
        self.root.resizable(False, False)

        self.frameSeats = tk.Frame(self.root, padx=10, pady=10)
        self.frameSeats.pack()

        self.statusVar = tk.StringVar()
        self.statusVar.set("Select a seat to reserve.")
        self.labelStatus = tk.Label(self.root, textvariable=self.statusVar, padx=10, pady=10)
        self.labelStatus.pack()

        self.updateSeats()

        self.root.mainloop()

if __name__ == "__main__":
    system = SeatReservationSystem(5, 10)
    system.start()
