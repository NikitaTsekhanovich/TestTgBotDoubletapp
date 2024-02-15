from django.core.management.base import BaseCommand
from django.conf import settings

from app.internal.models.admin_user import AdminUser

import telebot


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        bot = telebot.TeleBot(settings.TOKEN)

        @bot.message_handler(commands=['start'])
        def main(message):
            bot.send_message(message.chat.id, "Здарова!")
            bot.send_message(message.chat.id, f"{message.from_user.id}")
            bot.send_message(message.chat.id, f"{message.from_user.first_name}")
            bot.send_message(message.chat.id, f"{message.from_user.last_name}")
            bot.send_message(message.chat.id, f"{message.from_user.username}")

            p, f = AdminUser.objects.get_or_create(
                external_id=message.from_user.id,
                # username=message.from_user.username,
                # first_name=message.from_user.first_name,
                # last_name=message.from_user.last_name,
                defaults={
                    "first_name": message.from_user.first_name
                },
            )
            print(p)
            print(f)
        bot.polling(none_stop=True)
