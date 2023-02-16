import json

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from datetime import datetime
from utils import get_weather_days,read_json


from utils import get_weather_days

days_btn = ReplyKeyboardMarkup(row_width=True)


cities=["istanbul","moscow","newyork","tashkent"]

def get_btns():

    cities_inline_btn = InlineKeyboardMarkup()


    temp_keys = list()
    for key in cities:
        if len(temp_keys) % 2 == 0:
            cities_inline_btn.add(*temp_keys)
            temp_keys = list()

        temp_keys.append(InlineKeyboardButton(key, callback_data=f"cities_{key}"))

    if len(temp_keys) > 0:
        cities_inline_btn.add(*temp_keys)
    return cities_inline_btn

def get_days():
    temp=read_json("5505152487.json")
    city_name=temp.get("city")


    days_inline_btn = InlineKeyboardMarkup()


    temp_keys = list()
    for day in  get_weather_days(f"{city_name}.json"):
        formatted_day = datetime.strptime(day, "%Y.%m.%d").strftime("%b %d %Y")
        if len(temp_keys) % 2 == 0:
            days_inline_btn.add(*temp_keys)
            temp_keys = list()

        temp_keys.append(InlineKeyboardButton(formatted_day, callback_data=f"Feb_{formatted_day}"))

    if len(temp_keys) > 0:
        days_inline_btn.add(*temp_keys)
    return days_inline_btn
