import json

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def get_btns(action):
    with open("currency.json", "r") as f:
        file_content = f.read()
    currency_data = json.loads(file_content)

    currency_inline_btn = InlineKeyboardMarkup()

    keys = list(currency_data.get("data").keys())

    temp_keys = list()
    for key in keys:
        if len(temp_keys) % 3 == 0:
            currency_inline_btn.add(*temp_keys)
            temp_keys = list()

        temp_keys.append(InlineKeyboardButton(key, callback_data=f"{action}_currency_{key}"))

    if len(temp_keys) > 0:
        currency_inline_btn.add(*temp_keys)
    return currency_inline_btn
