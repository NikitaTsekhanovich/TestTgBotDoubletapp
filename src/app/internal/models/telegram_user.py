from django.db import models


class TelegramUser(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="ID пользователя в телеграме",
        default=0,
        unique=True
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name="Номер телефона",
        default=00000000000
    )
    username = models.CharField(
        max_length=40,
        verbose_name="Ник в телеге",
        default=''
    )
    first_name = models.CharField(
        max_length=40,
        verbose_name="Имя",
        default=''
    )
    last_name = models.CharField(
        max_length=40,
        verbose_name="Фамилия",
        default=''
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Id telegram: {self.external_id}.\n" \
               f"Number phone: {self.phone_number}"
