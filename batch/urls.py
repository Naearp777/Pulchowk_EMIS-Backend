from django.urls import path
from .import views

urlpatterns = [
    path('api/show_batch', views.show_batch , name = "show_batch" ),
    path('api/add_batch', views.add_batch , name = "add_batch" ),
    path('api/destroy_batch/<int:pk>', views.DestroyBatch.as_view()  ),
]
