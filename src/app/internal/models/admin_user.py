from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminUser(AbstractUser):
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

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"Id telegram: {self.external_id}.\nNumber phone: {self.phone_number}"
