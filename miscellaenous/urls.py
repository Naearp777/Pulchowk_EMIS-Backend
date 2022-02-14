from django.urls import path
from .import views
urlpatterns = [

   path('api/user/change_password/<int:u_id>/', views.password_reset, name='password_reset_firsttime'),
]