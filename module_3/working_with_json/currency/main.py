import json
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, StringVar, OptionMenu,PhotoImage
from PIL import Image,ImageTk
import requests
import datetime

KEY = "gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"

url = f"https://api.freecurrencyapi.com/v1/latest"

resp = requests.get(
    url,
    params={"apikey": KEY}
)
data_currency = json.loads(resp.text)

window = Tk()
window.title("Currency convertor ")
window.geometry("700x700")
window.configure(bg="thistle")


def convert():
    from_ = clicked1.get()
    to_ = clicked2.get()
    text_ = entry1.get()
    currency_dict=data_currency.get("data")
    result_text=float(currency_dict.get(f"{to_}")) / float(currency_dict.get(f"{from_}")) * float(text_)
    res_label = Label(window, width=40, text=f"{text_} {from_}={result_text} {to_}",height=2,  bg="yellow",fg="green")
    res_label.place(x=100, y=540)

def vice_versa():
    from_ = clicked1.get()
    to_ = clicked2.get()
    clicked1.set(to_)
    clicked2.set(from_)
    clear()




def clear():
    entry1.delete(0, END)
    res_label = Label(window, width=40, text="",bg="thistle",height=2,)
    res_label.place(x=100, y=540)



# icon=PhotoImage(file="currenc.png")
# icon.config(height=100,width=200)
# icon_label=Label(image=icon)
# icon_label.pack()

img=(Image.open("currenc.png"))

resized_image=img.resize((100,80),Image.ANTIALIAS)
icon=ImageTk.PhotoImage(resized_image)
icon_label=Label(image=icon,bg="thistle")
icon_label.place(x=150,y=30)



convert_label = Label(window, text="Currency exchange rate", font=25, bg="thistle", fg="blue")
convert_label.place(x=250, y=50)

amount_label=Label(window,bg="thistle",text="Amount",font=14,fg="green")
amount_label.place(x=100,y=140)

entry1 = Entry(window, width=45)
entry1.config(borderwidth=10, bg="lightcyan")
entry1.place(x=100, y=170)




from_label=Label(window,bg="thistle",text="From", font=14,fg="green")
from_label.place(x=100,y=250)


# Dropdown menu options

options = list(data_currency.get("data").keys())

# datatype of menu text
clicked1 = StringVar()

# Initial menu text
clicked1.set("USD")

# Create Dropdown menu
drop1 = OptionMenu(window, clicked1, *options)
drop1.config(width=40, height=2, bg="mediumaquamarine", fg="coral", )
drop1.place(x=100, y=280)

img_vise=(Image.open("66.png"))

resized=img_vise.resize((30,40),Image.ANTIALIAS)
icon_=ImageTk.PhotoImage(resized)

vice_btn = Button(window,image=icon_, font=3,  bg="thistle",fg="green",command=vice_versa)
vice_btn.place(x=200, y=360)


to_label=Label(window,bg="thistle",text="To", font=14,fg="green")
to_label.place(x=100,y=410)

clicked2 = StringVar()
clicked2.set("RUB")
drop2 = OptionMenu(window, clicked2, *options)
drop2.config(width=40, height=2, bg="mediumaquamarine", fg="coral")
drop2.place(x=100, y=440)

result_btn = Button(window, text="Convert", width=40,height=2, bg="thistle", fg="red",command=convert)
result_btn.place(x=100, y=510)

res_label = Label(window, width=40, text="result ...",  height=2,bg="aqua", fg="green")
res_label.place(x=100, y=570)



clear_btn = Button(window, text="clear", width=40, height=2,bg="thistle", fg="green",command=clear)
clear_btn.place(x=100, y=620)





if __name__ == "__main__":
    window.mainloop()
