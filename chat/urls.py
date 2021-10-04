from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', apiOverview, name='apiOverview'),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name="token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('api/room/', Rooms.as_view(), name="room"),
    path('api/dialog/', Dialog.as_view(), name="dialog"),
    path('api/users/', AddUsersRoom.as_view(), name="users"),

]
