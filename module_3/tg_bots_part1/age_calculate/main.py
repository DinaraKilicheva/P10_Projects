import datetime
from datetime import date

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

from module_3.tg_bots_part1.currency.keybords import get_btns
from utils import get_fullname, write_json, read_json

env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    msg = bot.send_message(chat_id, f"Wellcome to age calculate bot, {fullname}")
    bot.register_next_step_handler(msg, show_calendar)


@bot.message_handler(commands=["calculate"])
def show_calendar(m):
    calendar, step = DetailedTelegramCalendar().build()

    bot.send_message(m.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)

    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}", c.message.chat.id, c.message.message_id, reply_markup=key)
    elif result:
        age_year = datetime.date.strftime(result, "%Y-%m-%d").split("-")[0]
        result = datetime.datetime.now().year - int(age_year)

        bot.edit_message_text(f"You are  {result} years old", c.message.chat.id, c.message.message_id)







def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/calculate", "Choose currency")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
