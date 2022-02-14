from django.urls import path
from .import views
urlpatterns = [
    path('api/create/folder/<int:c_id>/<int:t_id>/' , views.create_folder, name='create_folder'),
    path('api/upload/materials/<int:f_id>/' , views.upload_materials, name='upload_materials'),
    

    
]