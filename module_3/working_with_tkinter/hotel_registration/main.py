import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar, IntVar
from tkcalendar import DateEntry
import tkinter as tk

from client import Client

bg = 'lightblue'

window = Tk()
window.title("Hotel Registration")
window.geometry("700x400")
window.configure(bg=bg)

clients = []


def add():
    add_btn["state"] = tk.NORMAL
    client = Client(
        name_entry.get(),
        age_entry.get(),
        address_entry.get(),
        length_entry.get(),
        payment_entry.get(),
    )
    if None in [client.name, client.age, client.address, client.length_stay, client.payment]:
        messagebox.showinfo("Please fill all the fields then press button")

    else:
        add_btn["state"] = tk.DISABLED
        clients.append(client.get_info(flag=True))
        messagebox.showinfo("Information", "The data has been added successfully")
        clients.append(client.get_info(flag=True))
        messagebox.showinfo("Information", "The data has been added successfully")


def save():
    save_btn["state"]=tk.NORMAL
    if add_btn["state"] == tk.DISABLED:
        save_btn["state"]=tk.DISABLED
        with open("clients.csv", "a", newline="\n") as file:
            header = ["Name", "Age", "Address", "Length stay", "Payment"]
            csv_writer = csv.DictWriter(file, header)
            if os.path.getsize("clients.csv") == 0:
                csv_writer.writeheader()
            csv_writer.writerows(clients)
        messagebox.showinfo("Information", "Saved successfully")
        clear()
    else:
        messagebox.showinfo("Please first press the add button")


def clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    length_entry.delete(0, END)
    payment_entry.delete(0, END)


# Hotel registration


# Name
name_label = Label(window, text="Name: ", fg="blue", font=2, bg=bg)
name_label.grid(row=1, column=0)
name_entry = Entry(window, width=50, borderwidth=4)
name_entry.grid(row=1, column=1)

# Age
age_label = Label(window, text="Age: ", fg="blue", font=2, bg=bg)
age_label.grid(row=2, column=0)
age_entry = Entry(window, width=50, borderwidth=4, highlightcolor="red")
age_entry.grid(row=2, column=1)

# Address
address_label = Label(window, text="Address ", fg="blue", font=2, bg=bg)
address_label.grid(row=4, column=0)
address_entry = Entry(window, width=50, borderwidth=4, highlightcolor="red")
address_entry.grid(row=4, column=1)

# Length of stay
length_label = Label(window, text="Length of stay: ", fg="blue", font=2, bg=bg)
length_label.grid(row=6, column=0)
length_entry = Entry(window, width=50, borderwidth=4, highlightcolor="red")
length_entry.grid(row=6, column=1)

# Payment
payment_label = Label(window, text="Payment: ", fg="blue", font=2, bg=bg)
payment_label.grid(row=7, column=0)
payment_entry = Entry(window, width=50, borderwidth=4, highlightcolor="red")
payment_entry.grid(row=7, column=1)

# Save button
save_btn = Button(window, text="Save", fg="blue", font=2, pady=10, padx=20, bg="gray", command=save)
save_btn.place(x=100, y=250)

# Add button
add_btn = Button(window, text="Add", fg="blue", font=2, padx=20, pady=10, bg="gray", command=add)
add_btn.place(x=210, y=250)

# Clear button
clear_btn = Button(window, text="Clear", fg="blue", font=2, padx=20, pady=10, bg="gray", command=clear)
clear_btn.place(x=310, y=250)

# Exit button
exit_btn = Button(window, text="Exit", fg="red", font=2, padx=20, pady=10, bg="gray", command=window.quit)
exit_btn.place(x=420, y=250)

if __name__ == "__main__":
    window.mainloop()
