from django.urls import path
from .import views
urlpatterns = [

    path('api/register/department/', views.createdepartment, name='register_department'),
    path('api/view/department/', views.Department_display_all, name='view_department'),
]