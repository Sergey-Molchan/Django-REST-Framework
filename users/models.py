from django.db import models
from django.contrib.auth.models import AbstractUser


class USer(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите почту"
    )
    tg_name = models.CharField(
        max_length=35,
        unique=True,
        verbose_name="Телеграмм",
        help_text="Введите телеграмм ник",
    )
    city = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите ваш город",
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите ваш номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите свое фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


