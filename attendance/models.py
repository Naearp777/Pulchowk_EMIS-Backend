from django.db import models
from student.models import student_info
from classes.models import classes
# Create your models here.
class Attendance(models.Model):
    classes=models.ForeignKey(classes, on_delete=models.CASCADE)
    student = models.ForeignKey(student_info, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=10, choices=[("P", "Present"), ("A", "Absent")])

    def __str__(self):
        return f"{self.student}--{self.date}--{self.time}--{self.status}"

    class Meta:
        verbose_name_plural = "attendance"