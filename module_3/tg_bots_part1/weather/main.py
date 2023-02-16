import json

import requests
import datetime
from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

from keybords import get_btns
from module_3.tg_bots_part1.weather.keybords import get_days
from utils import get_fullname, write_json, read_json, get_weather_days

env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Wellcome to weather info bot, {fullname}")


@bot.message_handler(commands=["city"])
def from_convert_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Choose city please...", reply_markup=get_btns())


@bot.callback_query_handler(lambda call: call.data.startswith("cities_"))
def from_currency_query_handler(call):
    message = call.message
    cities_name = call.data.split("_")[1]

    write_json(f"{message.chat.id}.json", {
        "city": cities_name
    })

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Choose date for weather forecast", reply_markup=get_days())


@bot.callback_query_handler(lambda call: call.data.startswith("Feb_"))
def to_currency_query_handler(call):
    message = call.message
    choosen_date = call.data.split("_")[1]
    storage = read_json(f"{message.chat.id}.json")
    date = datetime.strptime(choosen_date, "%b %d %Y").strftime("%Y.%m.%d")
    city = storage.get("city")
    city_data = read_json(f"{city}.json")
    for data in city_data:
        if data.get("day") == date:
            avg_temp = data.get("average_temperature")
    bot.send_message(message.chat.id, str(avg_temp))

    write_json(f"{message.chat.id}.json", storage)

    bot.delete_message(message.chat.id, message.id)




def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/city", "Choose city")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
