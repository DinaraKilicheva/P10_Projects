import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from tkcalendar import DateEntry
from datetime import datetime

window = Tk()
window.title("Age calculator")
window.geometry("700x350")
window.configure(bg="lightblue")


def calculate():
    return datetime.now().year-int(date_entry.get().split("/")[2])


def result():
    age = calculate()
    result_label = Label(window, text=f"Your age:{age}", bg="lightblue", font=14)
    result_label.place(x=80, y=170)


def submit():
    result()


age_label = tk.Label(window, text="Age calculator ", bg="lightblue", fg="orange", font=25)
age_label.place(x=295, y=10)

# Age date
date_label = Label(window, text="Birth year:", bg="grey", font=14)
date_label.place(x=80, y=50)
date_entry = DateEntry(window, locale="en_US", font="Arial 14", date_pattern="dd/MM/yyyy")
date_entry.place(x=200, y=50)

# Calculate age button
calc_btn = Button(window, text="Calculate age", bg="green", font=7, border=0,command=submit)
calc_btn.place(x=80, y=110)

if __name__ == "__main__":
    window.mainloop()
