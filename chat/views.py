from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    """
    Get, post, put, delete методы, аутентификация через JWS токены через 'Postman'
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)

    def perform_create(self, serializer):
        serializer.save( created_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def delete(self, request):
        return self.destroy(request, id)


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

        return Response(user_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def apiOverview(request):
    """
    Навигация по сайту
    """
    api_urls = {
        'Registration': 'http://127.0.0.1:8000/api/register/',
        'Login/Token gain-refresh': 'http://127.0.0.1:8000/api/token/',
        'Admin login': 'http://127.0.0.1:8000/admin',
        'All messages': 'http://127.0.0.1:8000/api/message-list/',
        'Details for 1 message': 'http://127.0.0.1:8000/api/message-detail/<int:pk>/',
        'Message create': 'http://127.0.0.1:8000/api/message-create/',
        'Message update': 'http://127.0.0.1:8000/api/message-update/<int:pk>/',
        'Generic Api View': 'http://127.0.0.1:8000/api/generic/<int:id>/Postman only',

    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    """ Показать все обращения """
    message = Message.objects.all()
    serializer = MessageSerializer(message, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewMessage(request, pk):
    """ Показать конктреное обращение"""
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateMessage(request):
    """ Создать обращение """
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateMessage(request, pk):
    """ Обновить обращение"""
    message = Message.objects.put(id=pk)
    serializer = MessageSerializer(instance=message, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

