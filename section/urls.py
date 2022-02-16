from django.urls import path
from . import views

urlpatterns = [
    path("api/view/section/", views.section_display_all, name="view_section"),
    path("api/create/section/", views.section_create, name="create_section"),
    path("api/update/section/<int:id>/", views.section_update, name="update_section"),
    path("api/delete/section/<int:id>/", views.section_delete, name="delete_section"),
]
