from django.urls import path
from .import views
urlpatterns = [

    path('api/view/batch/', views.Batch_display_all, name='view_batch'),
]