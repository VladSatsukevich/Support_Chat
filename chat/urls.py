from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', apiOverview, name='apiOverview'),
    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/generic/<int:id>/', GenericAPIView.as_view()),
    path('api/message-list/', ShowAll, name='message-list'),
    path('api/message-detail/<int:pk>/', ViewMessage, name='message-detail'),
    path('api/message-create/', CreateMessage, name='message-create'),
    path('api/message-update/<int:pk>/', updateMessage, name='message-update'),

]
