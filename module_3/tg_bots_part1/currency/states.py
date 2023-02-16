import telebot.handler_backends


class CurrencyConvertForm(telebot.handler_backends.StatesGroup):
    from_ = telebot.handler_backends.State()
    to_ = telebot.handler_backends.State()
