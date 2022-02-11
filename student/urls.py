from django.urls import path
from .import views
urlpatterns = [

    path('api/show/all_students/', views.show_all_students, name='show_all_students'),
    
]