import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from django.urls import reverse, path
from .serializers import *


class ChatTests(APITestCase):

    def test_chat_message(self):
        response = self.client.get(reverse("dialog"))
        print(response.data)
