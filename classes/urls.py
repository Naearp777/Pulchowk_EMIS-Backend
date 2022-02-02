from django.urls import path
from .import views
urlpatterns = [

    path('api/create/class/', views.create_class, name='create_class'),
    path('api/show/<int:pk>', views.show_class, name='show_class'),
]