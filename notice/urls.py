from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/notice/create/<int:c_id>/<int:t_id>/",
        views.createnotice_teacher,
        name="createnotice",
    ),
    path("api/notice/show/<int:c_id>/", views.show_notice, name="show_notice"),
    path(
        "api/notice/global/create/",
        views.create_globalnotice,
        name="create_globalnotice",
    ),
    path(
        "api/notice/show/global/detail/<int:pk>/",
        views.show_globalnotice,
        name="show_globalnotice",
    ),
    path(
        "api/notice/show/global/all/",
        views.show_all_globalnotices,
        name="show_all_globalnotices",
    ),
    path("api/notice/update/<int:pk>/", views.update_notice, name="update_notice"),
    path("api/notice/delete/<int:pk>/", views.delete_notice, name="delete_notice"),
    path(
        "api/notice/global/delete/<int:pk>/",
        views.delete_globalnotice,
        name="delete_globalnotice",
    ),
    path(
        "api/notice/global/update/<int:pk>/",
        views.update_globalnotice,
        name="update_globalnotice",
    ),
    path(
        "api/notice/dept/create/", views.create_deptnotice, name="create_deptnotice"
    ),
    path(
        "api/notice/dept/show/<int:pk>/", views.show_deptnotice, name="show_deptnotice"
    ),
    path(
        "api/notice/dept/show/all/<str:alias>/", views.show_deptnotice_all_for_a_dept, name="show_deptnotice_all_for_a_dept"
    )
]
