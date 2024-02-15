from django.conf import settings
from app.internal.models.telegram_user import TelegramUser

import telebot
import re


class Bot:
    def main(self):
        bot = telebot.TeleBot(settings.TOKEN)

        @bot.message_handler(commands=['start'])
        def add_user_database(message):
            bot.send_message(message.chat.id, "Здарова!")

            info_profile, is_new = TelegramUser.objects.get_or_create(
                external_id=message.from_user.id,

                defaults={
                    "username": message.from_user.username,
                    "first_name": message.from_user.first_name,
                    "last_name": message.from_user.last_name
                    if message.from_user.last_name is not None
                    else "None"
                },
            )
            if is_new:
                bot.send_message(message.chat.id, f"{message.from_user.first_name}, "
                                                  f"вы добавлены в базу")
            else:
                bot.send_message(message.chat.id, f"{message.from_user.first_name}, "
                                                  f"вы есть в базе")

        @bot.message_handler(commands=['set_phone'])
        def get_number_phone(message):
            response = bot.send_message(message.chat.id, "Введите номер телефона")
            bot.register_next_step_handler(response, set_number_phone)

        def set_number_phone(message):
            is_number_phone = re.match(
                r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                message.text)

            if is_number_phone:
                try:
                    user = TelegramUser.objects.get(external_id=message.from_user.id)
                    user.phone_number = message.text
                    user.save()
                    bot.send_message(message.chat.id, "Телефон добавлен в базу")
                except Exception as e:
                    print(e)
                    bot.send_message(message.chat.id, "Вас нет в базе. Введите команду /start")

            elif message.text == "/set_phone":
                get_number_phone(message)

            elif message.text == "/start":
                add_user_database(message)

            else:
                response = bot.send_message(message.chat.id, "Не верный ввод")
                bot.register_next_step_handler(response, set_number_phone)

        @bot.message_handler(commands=['me'])
        def get_me(message):
            try:
                user = TelegramUser.objects.get(external_id=message.from_user.id)
                bot.send_message(message.chat.id, f"{user.first_name}\n"
                                                  f"{user.last_name}\n"
                                                  f"{user.username}\n"
                                                  f"{user.phone_number}")
            except Exception as e:
                print(e)
                bot.send_message(message.chat.id, "Вас нет в базе. Введите команду /start")

        bot.polling(none_stop=True)
