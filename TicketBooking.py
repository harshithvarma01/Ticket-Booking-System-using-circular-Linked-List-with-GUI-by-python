import tkinter as tk
from tkinter import messagebox

class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seat Booking System")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        self.seats = {}  
        self.seat_price = 100
        self.booked_seats = []
        self.label = tk.Label(root, text="Seat Booking System", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=10)
        self.seat_frame = tk.Frame(root, bg="#f0f0f0")
        self.seat_frame.pack(pady=20)

        self.create_seat_grid()
        self.selected_label = tk.Label(root, text="Selected Seats: None", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.selected_label.pack(pady=5)

        self.price_label = tk.Label(root, text="Total Price: $0", font=("Arial", 14), bg="#f0f0f0", fg="#333")
        self.price_label.pack(pady=5)
        self.buy_button = tk.Button(root, text="Buy", font=("Arial", 14, "bold"), bg="#4caf50", fg="#ffffff", activebackground="#45a049", activeforeground="#ffffff", command=self.buy_seats, state="disabled")
        self.buy_button.pack(pady=10, ipadx=10, ipady=5)
        self.cancel_button = tk.Button(root, text="Cancel Selection", font=("Arial", 14, "bold"), bg="#f44336", fg="#ffffff", activebackground="#e53935", activeforeground="#ffffff", command=self.cancel_selection, state="disabled")
        self.cancel_button.pack(pady=10, ipadx=10, ipady=5)
        self.refund_button = tk.Button(root, text="Cancel Booking and Refund", font=("Arial", 14, "bold"), bg="#ff9800", fg="#ffffff", activebackground="#ff5722", activeforeground="#ffffff", command=self.cancel_booking, state="disabled")
        self.refund_button.pack(pady=10, ipadx=10, ipady=5)
        self.selected_seats = [] 
    def create_seat_grid(self):
        rows, cols = 5, 5
        for i in range(rows):
            for j in range(cols):
                seat_id = f"R{i+1}C{j+1}"
                self.seats[seat_id] = "available"
                button = tk.Button(self.seat_frame, text=seat_id, font=("Arial", 10, "bold"), bg="#4caf50", fg="#ffffff", width=8, height=2,
                                   command=lambda sid=seat_id: self.select_seat(sid))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.seats[seat_id] = button
    def select_seat(self, seat_id):
        if self.seats[seat_id].cget("bg") == "#4caf50":  
            if seat_id not in self.selected_seats:
                self.selected_seats.append(seat_id)
                self.seats[seat_id].config(bg="#ffeb3b") 
            else:
                self.selected_seats.remove(seat_id)
                self.seats[seat_id].config(bg="#4caf50") 
            self.update_seat_info()
        elif self.seats[seat_id].cget("bg") == "#f44336":
            messagebox.showwarning("Unavailable", f"Seat {seat_id} is already booked.")
    def update_seat_info(self):
        if self.selected_seats:
            selected_seats_str = ", ".join(self.selected_seats)
            total_price = len(self.selected_seats) * self.seat_price
            self.selected_label.config(text=f"Selected Seats: {selected_seats_str}")
            self.price_label.config(text=f"Total Price: ${total_price}")
            self.buy_button.config(state="normal")
            self.cancel_button.config(state="normal")
        else:
            self.selected_label.config(text="Selected Seats: None")
            self.price_label.config(text="Total Price: $0")
            self.buy_button.config(state="disabled")
            self.cancel_button.config(state="disabled")

    def cancel_selection(self):
        for seat in self.selected_seats:
            self.seats[seat].config(bg="#4caf50")
        self.selected_seats = []
        self.update_seat_info()
    def buy_seats(self):
        if self.selected_seats:
            for seat in self.selected_seats:
                self.seats[seat].config(bg="#f44336", state="disabled")
                self.booked_seats.append(seat)  
            total_price = len(self.selected_seats) * self.seat_price
            messagebox.showinfo("Success", f"Seats {', '.join(self.selected_seats)} booked successfully for ${total_price}!")
            self.selected_seats = []  
            self.update_seat_info()
            self.refund_button.config(state="normal")
    def cancel_booking(self):
        if self.booked_seats:
            for seat in self.booked_seats:
                self.seats[seat].config(bg="#4caf50", state="normal") 
            total_refund = len(self.booked_seats) * self.seat_price
            messagebox.showinfo("Refund", f"Booking for seats {', '.join(self.booked_seats)} has been canceled. You will be refunded ${total_refund}!")
            self.booked_seats = []  # Clear booked seats list
            self.refund_button.config(state="disabled")  # Disable refund button after cancellation
            self.update_seat_info()  # Reset the seat info

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingApp(root)
    root.mainloop()
