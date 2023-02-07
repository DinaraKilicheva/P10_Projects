import json
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, StringVar, OptionMenu, PhotoImage
from PIL import Image, ImageTk
from main import WeatherManager
import requests
import datetime

window = Tk()
window.title("Currency convertor ")
window.geometry("700x700")
window.configure(bg="thistle")


def show():
    text_label = Label(window, text="Average Temperature: ", width=50, height=3, bg="thistle", fg="green", )
    text_label.place(x=250, y=250, )
    date = clicked_date.get()
    avg = ""
    options_hours = []
    clicked_hour = StringVar()
    # Initial menu text
    clicked_hour.set("12:00")

    for days in info:
        if days["day"] == date:
            avg = days.get("average_temperature")
            avg_label = Label(window, text=avg, width=10, height=3, bg="thistle", )
            avg_label.place(x=500, y=250)
            for hour in days["hours"]:
                hour_ = hour.get("time")
                temperature = hour.get("temperature")
                options_hours.append(hour_)
                temp_label = Label(window, text=temperature, width=20, height=3, bg="thistle", fg="green", font=3)
                temp_label.place(x=250, y=470)
        hour_label = Label(window, text="Hour: ", width=20, height=3, bg="thistle", fg="green", font=3)
        hour_label.place(x=30, y=370)
        tem_label = Label(window, text="Temperature:", width=20, height=3, bg="thistle", fg="green", font=3)
        tem_label.place(x=30, y=470)

    hour_drop = OptionMenu(window, clicked_hour, *options_hours)
    hour_drop.config(width=30, height=2, bg="lavender", fg="coral", )
    hour_drop.place(x=180, y=400)
    city_name = clicked1.get().lower()


# Create Dropdown menu



# data = get_info()


# def clear():
#     icon_label.delete(0, END)


# icon=PhotoImage(file="currenc.png")
# icon.config(height=100,width=200)
# icon_label=Label(image=icon)
# icon_label.pack()

img = (Image.open("icon.png"))

resized_image = img.resize((100, 80), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(resized_image)
icon_label = Label(image=icon, bg="thistle")
icon_label.place(x=140, y=30)

weather_label = Label(window, text="Weather forecast App", font=25, bg="thistle", fg="blue")
weather_label.place(x=250, y=50)

select_city_label = Label(window, bg="thistle", text="Select city", font=14, fg="green")
select_city_label.place(x=50, y=180)

# Dropdown menu options

options = ["Tashkent", "Samarkand", "Moscow", "Berlin", "Paris", "Sydney", "India", "Miami", "Rome"]

# datatype of menu text


clicked1 = StringVar()

# Initial menu text
clicked1.set("Tashkent")

# Create Dropdown menu
drop1 = OptionMenu(window, clicked1, *options)
drop1.config(width=30, height=2, bg="mediumaquamarine", fg="coral", )
drop1.place(x=180, y=170)

city_name = clicked1.get().lower()


# obj=WeatherManager(f"{city_name}")
# info = obj.get_daily_temperature()

def write_info():
    with open("city_info.json", "w") as f:
        city_name = clicked1.get().lower()
        obj = WeatherManager(f"{city_name}")
        info = obj.get_daily_temperature()
        json.dump(info.text, f)


def get_info():
    with open("date.json", "r") as f:
        data = json.load(f)

        return data


info = get_info()

option_days = []
for days in info:
    option_days.append(days["day"])

clicked_date = StringVar()

# Initial menu text
clicked_date.set("2023.02.07")

# Create Dropdown menu
drop_date = OptionMenu(window, clicked_date, *option_days)
drop_date.config(width=25, height=2, bg="lavender", fg="green", )
drop_date.place(x=50, y=250)

show_btn = Button(window, bg="lime", text="show", font=6, command=show)
show_btn.place(x=430, y=170)

# resized = img_vise.resize((30, 40), Image.ANTIALIAS)
# icon_ = ImageTk.PhotoImage(resized)
#
# vice_btn = Button(window, image=icon_, font=3, bg="thistle", fg="green", command=vice_versa)
# vice_btn.place(x=200, y=360)
#
# to_label = Label(window, bg="thistle", text="To", font=14, fg="green")
# to_label.place(x=100, y=410)
#
# clicked2 = StringVar()
# clicked2.set("RUB")
# drop2 = OptionMenu(window, clicked2, *options)
# drop2.config(width=40, height=2, bg="mediumaquamarine", fg="coral")
# drop2.place(x=100, y=440)
#
# result_btn = Button(window, text="Convert", width=40, height=2, bg="thistle", fg="red", command=convert)
# result_btn.place(x=100, y=510)
#
# res_label = Label(window, width=40, text="result ...", height=2, bg="aqua", fg="green")
# res_label.place(x=100, y=570)
#
# clear_btn = Button(window, text="clear", width=40, height=2, bg="thistle", fg="green", command=clear)
# clear_btn.place(x=100, y=620)

if __name__ == "__main__":
    window.mainloop()
