from django.urls import path
from . import views

urlpatterns = [
    path("api/assessement/import/<int:c_id>/", views.importassessment_csv, name="import_assessment"),
    path("api/assessement/export/<int:d_id>/", views.Export_Student_Class_list, name="export_student_class_list"),
    path("api/assessement/list/<int:c_id>/", views.get_assessment_list, name="get_assessment_list"),

]
  
