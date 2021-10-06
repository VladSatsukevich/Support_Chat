from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class Room(models.Model):
    """Модель запроса чата с поддержкой"""
    name = models.CharField(max_length=120, null=True, blank=False, verbose_name="Название обращения")
    creater = models.ForeignKey(User, verbose_name="Создатель обращения", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now_add=True)
    STATUS = (
        ('Нерешен', 'Нерешен'),
        ('Решен', 'Решен'),
        ('Замарожен', 'Замарожен'),
    )
    status = models.CharField(max_length=120, default='Нерешен', choices=STATUS, null=True, verbose_name="Статус")

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"


class Chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Room, verbose_name="Номер запроса", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение запроса"
        verbose_name_plural = "Сообщения запросов"
