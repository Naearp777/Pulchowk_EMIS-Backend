from django.urls import path
from . import views

urlpatterns = [
    path("api/view/batch/", views.Batch_display_all, name="view_batch"),
    path("api/create/batch/", views.Batch_create, name="create_batch"),
    path("api/update/batch/<int:id>/", views.Batch_update, name="update_batch"),
    path("api/delete/batch/<int:id>/", views.Batch_delete, name="delete_batch"),
]
