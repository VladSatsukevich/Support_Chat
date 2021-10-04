from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


class Rooms(APIView):
    """Комнаты запросов"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response({"status": "Успешно"})


class Dialog(APIView):
    """Диалог запроса, сообщение"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response({"status": "Сообщение отправлено"})
        else:
            return Response({"status": "Ошибка"})


class AddUsersRoom(APIView):
    """Добавление пользователя-ей в комнату чата"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)

class RegisterView(APIView):
    """
    Обычная регистрация, логин, почта, пароль
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=201)

@api_view(['GET'])
def apiOverview(request):
    """
    Навигация по сайту
    """
    api_urls = {
        'Регистрация': 'http://127.0.0.1:8000/api/register/',
        'Логин + Токен': 'http://127.0.0.1:8000/api/token/',
        'Админка': 'http://127.0.0.1:8000/admin',
        'Все возможные запросы': 'http://127.0.0.1:8000/api/room/',
        'Сам запрос': 'http://127.0.0.1:8000/api/dialog/',
        'Пользователи': 'http://127.0.0.1:8000/api/users/',
    }
    return Response(api_urls)
