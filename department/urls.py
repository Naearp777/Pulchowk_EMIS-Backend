from django.urls import path
from .import views
urlpatterns = [

    path('api/register/department/', views.createdepartment, name='register_department'),
    path('api/view/department/', views.Department_display_all, name='view_department'),
    path('api/view/department/<int:pk>/', views.Department_display_by_id, name='view_department_by_id'),
    path('api/view/department/<str:alias>/', views.Department_display_by_alias, name='view_department_by_alias'),
    path('api/update/department/<int:pk>/', views.Department_update, name='update_department'),
    path('api/delete/department/<int:pk>/', views.Department_delete, name='delete_department'),
]