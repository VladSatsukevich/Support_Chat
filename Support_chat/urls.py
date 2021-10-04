from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from chat.views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'room', Rooms, basename='rooms')
router.register(r'dialog', Dialog, basename='dialog')


urlpatterns = [
    path('viewset/register/', RegisterView.as_view({'post': 'create'}), name="register"),
    path('viewset/token/', TokenObtainPairView.as_view(), name="token"),
    path('viewset/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('viewset/', include(router.urls)),
    path('admin/', admin.site.urls),



]

urlpatterns += doc_urls