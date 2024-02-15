from .models.telegram_user import TelegramUser
from django.http import HttpResponse


def get_me(request, external_id):
    try:
        user = TelegramUser.objects.get(external_id=external_id)
        return HttpResponse(f'username: {user.first_name}, '
                            f'phone_number:{user.phone_number}')
    except Exception as e:
        print(e)
