from translate import Translator
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
from utils import get_fullname, write_json, read_json


env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Wellcome to translate bot, {fullname}")


@bot.message_handler(commands=["translate"])
def from_convert_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Choose language please...", reply_markup=get_btns("from"))


@bot.callback_query_handler(lambda call: call.data.startswith("from_language"))
def from_currency_query_handler(call):
    message = call.message
    translate_lang = call.data.split("_")[2]
    write_json(f"{message.chat.id}.json", {
        "from": translate_lang
    })

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Choose language to translate", reply_markup=get_btns("to"))


@bot.callback_query_handler(lambda call: call.data.startswith("to_language"))
def to_currency_query_handler(call):
    message = call.message
    translate_lang = call.data.split("_")[2]
    storage = read_json(f"{message.chat.id}.json")
    storage["to"] = translate_lang

    write_json(f"{message.chat.id}.json", storage)

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "Write a text you want to translate ...")


@bot.message_handler(content_types=["text"])
def get_amount(message):
    text = message.text
    storage = read_json(f"{message.chat.id}.json")
    key1 = storage.get("from")
    key2 = storage.get("to")
    translator = Translator(to_lang=f"{key1}")
    translation = translator.translate(text)

    bot.send_message(message.chat.id, translation)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/translate", "Choose translate language")
    ]



if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()

