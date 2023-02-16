import json
import requests
import telebot
from environs import Env
from telebot.types import BotCommand, ReplyKeyboardRemove

from module_3.tg_bots_part1.lotin_cyrillic.keybords import languages_inline_btn
from utils import get_fullname, write_json, read_json
from convert import *

env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Wellcome to Latin Cyrillic  bot, {fullname}")


@bot.message_handler(commands=["convert"])
def from_convert_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Choose convert  language please...", reply_markup=languages_inline_btn)


@bot.callback_query_handler(lambda call: call.data.startswith("language_"))
def from_currency_query_handler(call):
    message = call.message
    convert_from = call.data.split("_")[1]
    write_json(f"{message.chat.id}.json", {
        "from": convert_from
    })

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "please write a text ")


@bot.message_handler(content_types=["text"])
def get_amount(message):
    text_ = message.text
    storage = read_json(f"{message.chat.id}.json")
    from_ = storage.get("from")
    if from_ == "cyrillic":
        result_text = to_cyrillic(text_)
    else:
        result_text = to_latin(text_)
    bot.send_message(message.chat.id, result_text)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/convert", "Choose convert")
    ]



if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
