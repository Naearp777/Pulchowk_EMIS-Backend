from django.urls import path
from . import views

urlpatterns = [

    path('api/attendance/create/<int:c_id>/', views.importattendance_csv, name="import_attendance"),
    path('api/attendance/list/<int:c_id>/', views.get_attendance_list, name="get_attendance_list"),
    path('api/attendance/delete/<int:c_id>/', views.delete_attendance_list, name="delete_attendance_list"),
    path('api/attendance/list/<int:c_id>/<str:date>/', views.get_attendance_list_by_date, name="get_attendance_list_by_date"),

]