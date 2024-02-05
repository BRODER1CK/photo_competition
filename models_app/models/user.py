from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets


class User(AbstractUser):
    email = models.EmailField()
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    avatar = models.ImageField(max_length=255,
                               upload_to="web_site/%Y/%m/%d/",
                               blank=True,
                               null=True,
                               verbose_name="Фотография")
    token = models.CharField(max_length=255, default=secrets.token_hex(16), verbose_name="Токен")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
