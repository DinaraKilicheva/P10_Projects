import json

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

languages_inline_btn = InlineKeyboardMarkup()

languages_inline_btn.add(
    InlineKeyboardButton("Cyrillic",
                         callback_data=f"language_cyrillic"),
    InlineKeyboardButton("Latin",
                         callback_data=f"language_latin"),
)