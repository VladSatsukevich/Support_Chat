from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=8, min_length=4, write_only=True)
    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Сериализация комнат чата,
    Можно выбрать с кем из сапорта вести диалог или его автоматически назначат"""
    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("name", "status", "id", "creater", "invited", "date")


class ChatSerializers(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")

