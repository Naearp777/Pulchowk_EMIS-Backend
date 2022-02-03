from django.conf.urls import include
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view()),
    path('api/users/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
         
         ]