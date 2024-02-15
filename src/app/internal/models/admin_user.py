from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminUser(AbstractUser):
    external_id = models.PositiveIntegerField(
        verbose_name="ID пользователя в телеграме",
        default=0,
        unique=True
    )
    phone_number = models.PositiveIntegerField(
        verbose_name="Номер телефона",
        default=00000000000
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.external_id} {self.phone_number}"


# class Profile(models.Model):
#     external_id = models.PositiveIntegerField(
#         verbose_name="ID пользователя в соц сети"
#     )
#     name = models.TextField(
#         verbose_name="Имя пользователя"
#     )
#
#     class Meta:
#         verbose_name = "Профиль"
#         verbose_name_plural = "Профили"

