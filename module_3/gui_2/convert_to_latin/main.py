import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, StringVar, OptionMenu
from convert import *
from sample import student
from tkcalendar import DateEntry

window = Tk()
window.title("Convert from Latin to Cyrillic and vice versa ")
window.geometry("700x350")
window.configure(bg="thistle")


def convert():
    from_ = clicked1.get()
    to_ = clicked2.get()
    text_ = entry1.get()
    if from_ == "Latin" and to_ == "Cyrillic":
        result_text = to_cyrillic(text_)
        res_label = Label(window, width=20, text=result_text,borderwidth=10,bg="lightcyan")
        res_label.place(x=400, y=220)
    elif from_ == "Cyrillic" and to_ == "Latin":
        res_text = to_latin(text_)
        res_label = Label(window, width=20, text=res_text,borderwidth=10,bg="lightcyan")
        res_label.place(x=400, y=220)
    else:
        messagebox.showinfo("You choose the same option!!!")


def clear():
    entry1.delete(0, END)
    clicked1.set("Latin")
    clicked2.set("Cyrillic")
    res_label = Label(window, width=20, text="")
    res_label.place(x=400, y=220)


convert_label = Label(window, text="Convert from Latin to Cyrillic and vice versa", font=25, bg="thistle", fg="blue")
convert_label.place(x=150, y=50)

# Dropdown menu options
options = [
    "Latin",
    "Cyrillic"

]

# datatype of menu text
clicked1 = StringVar()

# Initial menu text
clicked1.set("Latin")

# Create Dropdown menu
drop1 = OptionMenu(window, clicked1, *options)
drop1.config(width=20, height=2, bg="mediumaquamarine", fg="coral", )
drop1.place(x=100, y=150)
entry1 = Entry(window, width=25)
entry1.config(borderwidth=10, bg="lightcyan")
entry1.place(x=100, y=220)

vice_btn = Button(window, text="<=>", font=3, width=6, height=1, bg="thistle", fg="green", command=convert)
vice_btn.place(x=280, y=150)

result_btn = Button(window, text="Convert", width=10, bg="thistle", fg="red", command=convert)
result_btn.place(x=280, y=220)

res_label = Label(window, width=22, text="",borderwidth=10)
res_label.place(x=400, y=220)

clear_btn = Button(window, text="clear", width=10, bg="thistle", fg="green", command=clear)
clear_btn.place(x=280, y=260)

clicked2 = StringVar()
clicked2.set("Cyrillic")

drop2 = OptionMenu(window, clicked2, *options)
drop2.config(width=20, height=2, bg="mediumaquamarine", fg="coral")
drop2.place(x=400, y=150)

if __name__ == "__main__":
    window.mainloop()
