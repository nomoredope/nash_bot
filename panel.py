from telebot import TeleBot

admin_panel_str = "\n/database_users - показать базу пользователей\n/alert - рассылка пользователям"

worker_panel_str = "\n/database_users - показать базу пользователей"


def admin_panel(message, usr,  temp_bot):
    temp_bot.send_message(message.chat.id, f"<b><u>Привет {usr} Админ!</u>\n"
                                           f"Доступные команды:</b>{admin_panel_str}", parse_mode="html")


def worker_panel(message, usr, temp_bot):
    temp_bot.send_message(message.chat.id, f"<b><u>Привет {usr} Работник!</u>\n"
                                           f"Доступные команды:</b>{worker_panel_str}", parse_mode="html")
