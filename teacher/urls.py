from django.urls import path
from . import views

urlpatterns = [
    path("api/show/all_teacher/", views.show_all_teacher, name="show_all_teacher"),
    path("api/show/teacher/by/dept/<str:alias>", views.show_teacher_by_department, name="show_teacher_by_department"),
    path("api/show/teacher/profile/<int:t_id>/", views.show_teacher_profile, name="show_teacher_profile"),
    path("api/get/students/for/a/teacher/<int:t_id>/", views.show_students_for_a_teacher, name="show_students_for_a_teacher"),
]
