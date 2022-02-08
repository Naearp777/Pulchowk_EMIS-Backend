from django.urls import path
from .import views
urlpatterns = [

    path('api/notice/create/', views.createnotice, name='createnotice'),
]