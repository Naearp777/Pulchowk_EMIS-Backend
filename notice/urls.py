from django.urls import path
from .import views
urlpatterns = [

    path('api/notice/create/<int:c_id>/', views.createnotice_teacher, name='createnotice'),
]