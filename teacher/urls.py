from django.urls import path
from . import views

urlpatterns = [
    path("api/show/all_teacher/", views.show_all_teacher, name="show_all_teacher"),
    path("api/show/teacher/by/dept/<str:alias>", views.show_teacher_by_department, name="show_teacher_by_department"),
]
