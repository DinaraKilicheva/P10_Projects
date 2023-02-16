from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)

#Start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Hi ,wellcome to convert bot {fullname}", reply_markup=languages_inline_btn)