from django.urls import path
from . import views

urlpatterns = [
    path("api/create/class/", views.create_class, name="create_class"),
    path("api/show/<int:pk>/", views.show_class, name="show_class"),
    path("api/show/all/", views.show_all_class, name="show_all_class"),
    path(
        "api/show/class/by/teacher/<int:pk>/",
        views.show_class_by_teacher,
        name="show_class_by_teacher",
    ),
    path(
        "api/show/class/by/student/<int:pk>/",
        views.show_class_by_student,
        name="show_class_by_student",
    ),
    path(
        "api/show/class/by/department/<int:pk>/",
        views.show_class_by_department,
        name="show_class_by_department",
    ),
    path("api/update/class/<int:pk>/", views.update_class, name="update_class"),
    path("api/delete/class/<int:pk>/", views.delete_class, name="delete_class"),
]
