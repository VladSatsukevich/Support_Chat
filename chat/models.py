from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class Room(models.Model):
    """Модель запроса чата с поддержкой"""
    name = models.CharField(max_length=120, null=True, blank=False, verbose_name="Title of the appeal")
    creater = models.ForeignKey(User, verbose_name="The creator of the appeal", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Participants", related_name="invited_user")
    date = models.DateTimeField("Date of creation", auto_now_add=True)
    Not_resolved = 'not resolved'
    Resolved = 'resolved'
    Frozen = 'frozen'
    STATUS = [
        (Not_resolved, 'not resolved'),
        (Resolved, 'resolved'),
        (Frozen, 'frozen'),
    ]
    status = models.CharField(max_length=120, default=Not_resolved, choices=STATUS, null=True, verbose_name="Status")

    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"


class Chat(models.Model):
    """Модель чата"""
    room = models.ForeignKey(Room, verbose_name="Request number", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date of shipment", auto_now_add=True)

    class Meta:
        verbose_name = "Request Message"
        verbose_name_plural = "Request Messages"
