from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/notification/show/all/specific/user/<int:pk>/",
        views.show_all_notification_to_user,
        name="show_all_notification_to_user",
    ),
]
