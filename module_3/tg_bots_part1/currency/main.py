import json

import requests
import datetime
from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

from module_3.tg_bots_part1.currency.keybords import get_btns
from utils import get_fullname, write_json, read_json
import states
from currency import Currency

KEY = "gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"

url = f"https://api.freecurrencyapi.com/v1/latest"

resp = requests.get(
    url,
    params={"apikey": KEY}
)
data_currency = json.loads(resp.text)

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
    bot.send_message(chat_id, f"Wellcome to convert bot, {fullname}")


@bot.message_handler(commands=["exchange"])
def from_convert_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Choose currency please...", reply_markup=get_btns("from"))


@bot.callback_query_handler(lambda call: call.data.startswith("from_currency_"))
def from_currency_query_handler(call):
    message = call.message
    currency_code = call.data.split("_")[2]
    write_json(f"{message.chat.id}.json", {
        "from": currency_code
    })

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "...", reply_markup=ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Choose currency to exchange", reply_markup=get_btns("to"))


@bot.callback_query_handler(lambda call: call.data.startswith("to_currency_"))
def to_currency_query_handler(call):
    message = call.message
    currency_code = call.data.split("_")[2]
    storage = read_json(f"{message.chat.id}.json")
    storage["to"] = currency_code

    write_json(f"{message.chat.id}.json", storage)

    bot.delete_message(message.chat.id, message.id)
    bot.send_message(message.chat.id, "Send  amount of currency please...")


@bot.message_handler(content_types=["text"])
def get_amount(message):
    amount = float(message.text)
    storage = read_json(f"{message.chat.id}.json")
    key1 = storage.get("from")
    key2 = storage.get("to")
    data = read_json("currency.json")
    from_ = data.get("data")[f"{key1}"]
    to_ = data.get("data")[f"{key2}"]
    result_text = round(to_ / from_ * float(amount), 2)
    bot.send_message(message.chat.id, result_text)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/exchange", "Choose currency")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
