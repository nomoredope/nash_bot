from telebot import TeleBot, types

admin_panel_str = "\nПоказать базу пользователей\nРассылка пользователям\nВывести " \
                  "текущую дату и время"

worker_panel_str = "\n/database_users - показать базу пользователей\n/date - вывести текущую дату и время"

user_panel_str = " посмотерть текущую дату и время."


def admin_panel(message, usr, temp_bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("База пользователей")
    button2 = types.KeyboardButton("Рассылка")
    button3 = types.KeyboardButton("Текущее время и дата")
    markup.add(button1, button2, button3)
    temp_bot.send_message(message.chat.id, f"Привет {usr} Админ!\n"
                                           f"Доступные команды:{admin_panel_str}",
                          parse_mode="html", reply_markup=markup)


def worker_panel(message, usr, temp_bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button4 = types.KeyboardButton("database_users")
    button5 = types.KeyboardButton("Текущее время и дата")
    markup.add(button4, button5)
    temp_bot.send_message(message.chat.id, f"Привет {usr} Работник!\n"
                                           f"Доступные команды:{worker_panel_str}",
                          parse_mode="html", reply_markup=markup)


def user_panel(message, usr, temp_bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button6 = types.KeyboardButton("Текущее время и дата")
    markup.add(button6)
    temp_bot.send_message(message.chat.id, f"Привет! Твоя роль Пользователь.\n"
                                           f"В данный момент ты можешь только {user_panel_str}",
                          parse_mode="html", reply_markup=markup)
