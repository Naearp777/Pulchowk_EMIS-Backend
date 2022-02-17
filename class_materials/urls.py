from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/create/folder/<int:c_id>/<int:t_id>/",
        views.create_folder,
        name="create_folder",
    ),
    path(
        "api/upload/materials/<int:f_id>/",
        views.upload_materials,
        name="upload_materials",
    ),
    path("api/show/folder/<int:pk>/", views.show_folder, name="show_folder"),
    path("api/update/folder/<int:pk>/", views.update_folder, name="update_folder"),
    path("api/delete/folder/<int:pk>/", views.delete_folder, name="delete_folder"),
    path(
        "api/show/all/folder/<int:c_id>/",
        views.show_all_folder_in_a_specific_class,
        name="show_all_folder_given__in_specific_class",
    ),
    path('api/show/all/materials/<int:f_id>/', views.show_materials_in_a_folder, name='show_all_materials_in_a_folder'),
]
