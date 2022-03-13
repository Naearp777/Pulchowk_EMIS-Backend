from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/user/change_password/<int:u_id>/",
        views.password_reset,
        name="password_reset_firsttime",
    ),
    path("api/filter/student/", views.filter_student.as_view(), name="filter_student"),
    path("api/filter/teacher/", views.filter_teacher.as_view(), name="filter_teacher"),
    path("api/show/admin/dashboard/", views.show_admin_dashboard, name="show_admin_dashboard"),
    path("api/show/student/dashboard/<int:pk>/", views.show_student_dashboard, name="show_student_dashboard"),
    path("api/show/teacher/dashboard/<int:pk>/", views.show_teacher_dashboard, name="show_teacher_dashboard"),
    path("api/evaluation/form/create/<int:pk>/", views.create_evaluation_form, name="create_evaluation_form"),
]
