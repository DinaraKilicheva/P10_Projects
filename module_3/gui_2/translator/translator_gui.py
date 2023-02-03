import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar, OptionMenu
from tkcalendar import DateEntry
from datetime import datetime
from translate import Translator

window = Tk()
window.title("Translator")
window.geometry("700x350")
window.configure(bg="yellowgreen")


def translate():
    language_ = clicked2.get()
    language = options[language_]
    translator = Translator(to_lang=language)
    text = entry1.get()
    translation = translator.translate(text)
    res_label = Label(window, width=20, text=translation)
    res_label.place(x=400, y=200)
    sentence = {
        "From language": "English",
        "Text": text,
        "TO language": language_,
        "Result": translation,
        "Date": datetime.now()

    }

    with open("sentence.csv", "a",encoding="utf_8_sig", newline="\n") as file:
        header = ["From language", "Text", "TO language", "Result", "Date"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("sentence.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerow(sentence)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    entry1.delete(0, END)
    clicked1.set("English")
    clicked2.set("Uzbek")
    res_label = Label(window, width=20, text="")
    res_label.place(x=400, y=200)


langueage_label = Label(window, text="Translator", font=25, bg="yellowgreen", fg="cyan")
langueage_label.place(x=270, y=50)

# Dropdown menu options
options = {
    "English": "en",
    "Russian": "ru",
    "Arabic": "ar",
    "Chinese": "zh",
    "German": "de",
    "French": "fr",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr",
    "Uzbek": "uz",

}
opt = list(options.keys())

# datatype of menu text
clicked1 = StringVar()

# Initial menu text
clicked1.set("English")

# Create Dropdown menu
drop1 = OptionMenu(window, clicked1, *opt)
drop1.config(borderwidth=8,width=20)
drop1.place(x=90, y=150)
entry1 = Entry(window, width=25)
entry1.config(borderwidth=8)
entry1.place(x=90, y=200)

tr_label = Label(window, text="=>", font=14, width=10, bg="yellowgreen")
tr_label.place(x=270, y=150)

result_btn = Button(window, text="Translate", width=10,height=2, bg="thistle", fg="steelblue", command=translate)
result_btn.place(x=280, y=200)

clear_btn = Button(window, text="clear", width=10,height=2, bg="thistle", fg="steelblue", command=clear)
clear_btn.place(x=280, y=250)

clicked2 = StringVar()
clicked2.set("Uzbek")

drop2 = OptionMenu(window, clicked2, *opt)
drop2.config(borderwidth=8,width=20)
drop2.place(x=400, y=150)

# # Age date
# date_label = Label(window, text="Birth year:", bg="grey", font=14)
# date_label.place(x=80, y=50)
# date_entry = DateEntry(window, locale="en_US", font="Arial 14", date_pattern="dd/MM/yyyy")
# date_entry.place(x=200, y=50)
#
# # Calculate age button
# calc_btn = Button(window, text="Calculate age", bg="green", font=7, border=0, command=submit)
# calc_btn.place(x=80, y=110)
#
if __name__ == "__main__":
    window.mainloop()
