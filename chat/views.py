from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import generics, status, viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


class Rooms(viewsets.ViewSet, generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Комнаты запросов"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)


class Dialog(viewsets.ViewSet, generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Диалог запроса, сообщение"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializers
    queryset = Chat.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        return self.list(request, id)

    def post(self, request, id=None):
        return self.create(request, id)


class RegisterView(viewsets.ViewSet, GenericAPIView, CreateModelMixin):
    """
    Обычная регистрация, логин, почта, пароль
    """
    serializer_class = RegisterSerializer
    queryset = RegisterSerializer
    lookup_field = 'id'

    def post(self, request, id=None):
        return self.create(request, id)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Просмотр существующих пользователей
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

