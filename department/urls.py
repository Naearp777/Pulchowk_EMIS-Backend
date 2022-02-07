from django.urls import path
from .import views
urlpatterns = [

    path('api/register/department/', views.createdepartment, name='register_department'),
]