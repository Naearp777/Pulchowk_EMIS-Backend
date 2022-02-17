from django.db import models
from classes.models import classes
from student.models import student_info
# Create your models here.
class Assessment(models.Model):
    classes=models.ForeignKey(classes, on_delete=models.CASCADE)
    student=models.ForeignKey(student_info, on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)
    
    def __str__(self):
        return self.student.rollno

    class Meta:
        verbose_name_plural = "Assessments"