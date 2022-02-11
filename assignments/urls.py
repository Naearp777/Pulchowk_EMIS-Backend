from django.urls import path
from .import views
urlpatterns = [

    path('api/assignment/create/<int:c_id>/<int:t_id>/', views.create_assignment, name='create_assignment'),
    path('api/assignment/submit/<int:a_id>/<int:s_id>/', views.submit_assignment, name='submit_assignment'),

]