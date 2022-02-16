from django.conf.urls import include
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("api/users/login/", views.MyTokenObtainPairView.as_view()),
    path("api/users/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('api/users/self/department/',
         views.get_self_department, name='self_department'),
    path("api/users/self/role", views.get_self_role, name="self_role"),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("logout/", views.LogoutView.as_view(), name="auth_logout"),
]
