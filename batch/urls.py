from django.urls import path
from .import views

urlpatterns = [
    path('api/show_batch', views.show_batch ),
]
