import json

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

options = {
    "English": "en",
    "Russian": "ru",
    "Arabic": "ar",
    "Chinese": "zh",
    "German": "de",
    "French": "fr",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr",
    "Uzbek": "uz",

}


def get_btns(action):
    translate_inline_btn = InlineKeyboardMarkup()

    keys = list(options.keys())

    temp_keys = list()
    for key,value in options.items():
        if len(temp_keys) % 3 == 0:
            translate_inline_btn.add(*temp_keys)
            temp_keys = list()

        temp_keys.append(InlineKeyboardButton(key, callback_data=f"{action}_language_{value}"))

    if len(temp_keys) > 0:
        translate_inline_btn.add(*temp_keys)
    return translate_inline_btn
