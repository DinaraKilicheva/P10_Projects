import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar, OptionMenu
from tkcalendar import DateEntry
from datetime import datetime
from translate import Translator
from pytube import YouTube

window = Tk()
window.title("Youtube mp4 downloader")
window.geometry("700x350")
window.configure(bg="indianred")

youtube_label = Label(window, text="Youtube mp4 downloader", font=25, bg="indianred", fg="darkseagreen")
youtube_label.place(x=250, y=50)

y_label = Label(window, text="Enter url", width=30, font=10, bg="indianred", fg="blue")
y_label.place(x=30, y=150)

url_entry = Entry(window, width=40)
url_entry.configure(borderwidth=8, bg="khaki")
url_entry.place(x=300, y=150)


def download():
    try:
        url = url_entry.get()
        YouTube(url).streams.first().download()
    except Exception as e:
        print(e)
    else:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        messagebox.showinfo("successfully downloaded")


result_btn = Button(window, text="download", font=7, bg="olive", fg="blue", command=download)
result_btn.place(x=250, y=230)



if __name__ == "__main__":
    window.mainloop()
