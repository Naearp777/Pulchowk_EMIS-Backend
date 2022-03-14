from django.urls import path
from . import views

urlpatterns = [

    path('api/attendance/create/<int:c_id>/', views.importattendance_csv, name="import_attendance"),
    path('api/attendance/create/<int:c_id>/<int:s_id>/', views.create_attendance, name="create_attendance"),
    path('api/attendance/list/<int:c_id>/', views.get_attendance_list, name="get_attendance_list"),
    path('api/attendance/delete/<int:c_id>/', views.delete_attendance_list, name="delete_attendance_list"),
    path('api/attendance/list/<int:c_id>/<str:date>/', views.get_attendance_list_by_date, name="get_attendance_list_by_date"),
    path('api/attendance/get/total/working/days/<int:c_id>/', views.get_total_working_days, name="get_total_working_days"),
    path('api/attendance/get/total/present/days/<int:c_id>/<int:s_id>/', views.get_student_present_days, name="get_total_present_days"),

]