from django.urls import path
from . import views

urlpatterns = [
    path('api/add_sem' , views.add_sem , name = "add_sem" ),
]
