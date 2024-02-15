from django.core.management.base import BaseCommand
from app.internal.transport.bot.handlers import Bot


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        bot = Bot()
        bot.main()
