from django.urls import path
from .import views
urlpatterns = [

    path('api/register/user/', views.registerUser, name='register_user'),
    path('api/export/user/', views.ExportUserCSV.as_view(), name='export_user'),
    path('api/import/user/', views.ImportUserCSV.as_view(), name='import_user'),
    path('api/users/update_profile/<int:u_id>/',views.update_profile,name='update_profile'),
    path('api/users/delete_profile/<int:u_id>/',views.delete_user,name='delete_profile'),
    path('api/users/show_profile/<int:u_id>/',views.get_user_by_id,name='show_profile'),
]