from django.urls import path
from .import views
urlpatterns = [

    path('api/notice/create/<int:c_id>/', views.createnotice_teacher, name='createnotice'),
    path('api/notice/show/<int:c_id>/', views.show_notice, name='show_notice'),
    path('api/notice/global/create/', views.create_globalnotice, name='create_globalnotice'),
    path('api/notice/show/global/<int:pk>/', views.show_globalnotice, name='show_globalnotice'),
    path('api/notice/update/<int:pk>/', views.update_notice, name='update_notice'),
    path('api/notice/delete/<int:pk>/', views.delete_notice, name='delete_notice'),
    path('api/notice/global/delete/<int:pk>/', views.delete_globalnotice, name='delete_globalnotice'),
    path('api/notice/global/update/<int:pk>/', views.update_globalnotice, name='update_globalnotice'),
  
]