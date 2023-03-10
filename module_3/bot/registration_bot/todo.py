from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

from keybords import share_phone_btn, get_language_btn, confirmation_inline_btn
from messages import messages
from states import StudentRegistrationForm
from task import Chat, Task
from utils import write_row_to_csv, get_fullname, get_language_code_by_chat_id

env = Env()
env.read_env(".env")

BOT_TOKEN = env("BOT_TOKEN")

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}", reply_markup=get_language_btn("register"))
    # bot.register_next_step_handler(message, set_language_handler)


# def set_language_handler(message):
#     chat = message.chat
#     new_chat = Chat(
#         chat.id,
#         get_fullname(chat.first_name, chat.last_name),
#         LANGUAGES.get(message.text)
#     )
#     write_row_to_csv(
#         "chats.csv",
#         list(new_chat.get_attrs_as_dict().keys()),
#         new_chat.get_attrs_as_dict()
#     )
#     bot.send_message(chat.id, messages[LANGUAGES.get(message.text)].get("add_task"), reply_markup=ReplyKeyboardRemove())


@bot.callback_query_handler(lambda call: call.data.startswith("register_language_"))
def set_language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[2]
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang_code
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang_code].get("add_task"))


@bot.message_handler(commands=["register"])
def register_student_handler(message):
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.set_state(message.from_user.id, StudentRegistrationForm.first_name, message.chat.id)


@bot.message_handler(state=StudentRegistrationForm.first_name)
def first_name_get(message):
    bot.send_message(message.chat.id, 'Familyangizni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.last_name)
def last_name_get(message):
    bot.send_message(message.chat.id, 'Telefon raqaminingizni yuboring:', reply_markup=share_phone_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.phone, content_types=["contact", "text"])
def phone_get(message):
    bot.send_message(message.chat.id, 'Yoshingizni kiriting:', reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, StudentRegistrationForm.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.contact.phone_number


@bot.message_handler(state=StudentRegistrationForm.age)
def age_get(message):
    bot.send_message(message.chat.id, 'Tilni kiriting:', reply_markup=get_language_btn("course"))
    bot.set_state(message.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    print(data)


@bot.callback_query_handler(lambda call: call.data.startswith("course_language_"),
                            state=StudentRegistrationForm.language)
def language_get(call):
    message = call.message
    # callback_data_example = "course_language_uz"
    lang_code = call.data.split("_")[2]
    msg = bot.send_message(message.chat.id, 'Kursni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['language'] = lang_code
    bot.register_next_step_handler(msg, course_get)
    print(data)


@bot.message_handler(state=StudentRegistrationForm.course)
def course_get(message):
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     data['course'] = message.text
    bot.send_message(message.chat.id, "ma'lumotlaringizni tastiqlang")
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['course'] = message.text
        msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
        msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
        msg += f"Phone: {data.get('phone')}\n"
        msg += f"Age: {data.get('age')}\n"
        msg += f"Language: {data.get('language')}\n"
        msg += f"Course: {data.get('course')}"
        student = {
            "First_name": data.get('first_name'),
            "Last_name": data.get('last_name'),
            "Phone": data.get('phone'),
            "Age": data.get('age'),
            "Language": data.get('language'),
            "Course": data.get('course')
        }
        write_row_to_csv("student.csv",list(student.keys()),student)
        print(student.get("Age"))
    bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=confirmation_inline_btn)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.callback_query_handler(lambda c: c.data.startswith("confirmation"))
def coursee_get(call):
    message = call.message
    # call_data_example = "confirm_course_yes"
    print(call.data)
    confirm_answer = call.data.split("_")[1]

    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     # data['course'] = message.text
    #     msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
    #     msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
    #     msg += f"Phone: {data.get('phone')}\n"
    #     msg += f"Age: {data.get('age')}\n"
    #     msg += f"Language: {data.get('language')}\n"
    #     msg += f"Course: {data.get('course')}"
    #     bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=confirmation_inline_btn)
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     student = {
    #     "First_name": data.get('first_name'),
    #     "Last_name": data.get('last_name'),
    #     "Phone": data.get('phone'),
    #     "Age": data.get('age'),
    #     "Language": data.get('language'),
    #     "Course": data.get('course')
    #     }
    # print(student.get("Age"))
    # if confirm_answewer == "yes":
        # write_row_to_csv("student.csv", list(student.keys()), student)
    #     bot.delete_state(message.from_user.id, message.chat.id)
    #     bot.delete_state(message.from_user.id, message.chat.id)
    # elif confirm_answer == "no":
    #     bot.send_message(message.chat.id, "Ma'lumotlar saqlanmadi qaytadan /register qiling")


    if confirm_answer == "yes":
        # write_row_to_csv("student.csv", list(student.keys()), student)
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.delete_state(message.from_user.id, message.chat.id)
    elif confirm_answer == "no":
        bot.send_message(message.chat.id, "Ma'lumotlar saqlanmadi qaytadan /register qiling")


# /add
@bot.message_handler(commands=["add"])
def add_task_handler(message):
    chat_id = message.chat.id
    lang_code = get_language_code_by_chat_id(chat_id, "chats.csv")
    msg = messages[lang_code].get("send_task")
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=["text"])
def get_task_handler(message):
    chat_id = message.chat.id
    if message.content_type != "text":
        bot.send_message(chat_id, "Invalid format.")

    new_task = Task(chat_id, message.text, datetime.now())
    write_row_to_csv(
        "tasks.csv",
        list(new_task.get_attrs_as_dict().keys()),
        new_task.get_attrs_as_dict()
    )

    bot.send_message(chat_id, "Add successfully.")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/add", "Add new task"),
        BotCommand("/register", "Register student")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
