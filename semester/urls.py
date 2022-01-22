from django.urls import path
from . import views

urlpatterns = [
    path('api/add_sem/' , views.add_sem , name = "add_sem" ),
    path('api/sem_detail/<int:pk>' , views.sem_detail , name = "sem_detail" ), #sem, update, delete,show
    path('api/create_sem/' , views.AddSem.as_view() , name = "create_sem" ),
]
