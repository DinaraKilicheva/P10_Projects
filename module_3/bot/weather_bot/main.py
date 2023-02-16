import json

from datetime import datetime

from telebot import TeleBot
from environs import Env
from telebot.types import BotCommand, ReplyKeyboardMarkup, KeyboardButton

# from api.weather import WeatherManager
# from bot.keyboards import days_btn
# from bot.student import Student
# from bot.utils import write_to_csv, is_exist_chat_id

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = TeleBot(BOT_TOKEN, parse_mode="html")


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    print(type(message))
    chat_id = message.chat.id
    user = message.from_user
    fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}")
    # if not is_exist_chat_id(chat_id):
    #     student = Student(chat_id, fullname)
    #     write_to_csv(student)
    # else:
    #     print("User already exist.")


@bot.message_handler()
def echo_text(message):
    chat_id = message.chat.id
    text = message.text

    buttons = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons.add(
        KeyboardButton('Birinchi'),
        KeyboardButton('Ikkinchi'),
        KeyboardButton('Uchinchi')
    )

    buttons.add(
        KeyboardButton('4'),
        KeyboardButton('5'),
        KeyboardButton('6')
    )

    bot.send_message(chat_id, text, reply_markup=buttons)


# /weather
# @bot.message_handler(commands=["weather"])
# def weather_handler(message):
#     today = datetime.now()
#     weather_data = WeatherManager("tashkent").get_daily_temperature()
#     today_weather = None
#     for day_weather in weather_data:
#         day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
#         if day_date.date() == today.date():
#             today_weather = day_weather
#     msg = f"<b>Bugungi ob-havo:</b>\n\n" \
#           f"<i>Harorat:</i> {today_weather.get('average_temperature')}"
#     bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=days_btn)

#
# @bot.message_handler(func=lambda message: message.text.startswith("Feb"))
# def day_weather_message(message):
#     date_msg = message.text
#     date = datetime.strptime(date_msg, "%b %d %Y")
#     weather_data = WeatherManager().get_daily_temperature()
#     weather = None
#     for day_weather in weather_data:
#         day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
#         if day_date.date() == date.date():
#             weather = day_weather
#     msg = f"<b>{date_msg} ob-havo:</b>\n\n" \
#           f"<i>Harorat:</i> {weather.get('average_temperature')}"
#     bot.reply_to(message, msg)
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)
#

def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/we", "Today weather")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
