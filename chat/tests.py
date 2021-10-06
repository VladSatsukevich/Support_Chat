import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from django.urls import reverse, path
from .serializers import *


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "Nick", "email": "user@example.com", "password": "12345"}
        response = self.client.post('/viewset/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ProfileViewTestCase(APITestCase):

    list_url = reverse('user-list')

    def setUp(self):
        self.user = User.objects.create_user(username="Mike", password="1234")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTPP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(200, response.status_code)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(403, response.status_code)
