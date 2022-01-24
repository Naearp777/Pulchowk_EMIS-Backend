from django.conf.urls import include
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),]