from django.urls import path
from .import views
urlpatterns = [

    path('api/show/all_teacher/', views.show_all_teacher    , name='show_all_teacher'),
    
]