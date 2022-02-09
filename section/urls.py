from django.urls import path
from .import views
urlpatterns = [

    path('api/view/section/', views.section_display_all, name='view_section'),
]