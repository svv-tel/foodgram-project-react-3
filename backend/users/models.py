from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    email = models.EmailField(
        'Электропочта',
        max_length=256,
        unique=True
    )

    username = models.CharField(
        'Никнэйм пользователя',
        max_length=128,
        unique=True
    )

    first_name = models.CharField(
        'Имя',
        max_length=128
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=128
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
