from django.urls import path
from .import views
urlpatterns = [

    path('api/register/user/', views.registerUser, name='register_user'),
    path('api/export/user/', views.ExportUserCSV.as_view(), name='export_user'),
    path('api/import/user/', views.ImportUserCSV.as_view(), name='import_user'),
]