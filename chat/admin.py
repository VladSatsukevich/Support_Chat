from django.contrib import admin
from . models import *

class RoomAdmin(admin.ModelAdmin):
    """Комнаты запросов"""
    list_display = ("name", "creater", "invited_user", "date", "status")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)

