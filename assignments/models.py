from classes.models import classes
from django.db import models

from customuser.models import User

# Create your models here.


class Give_Assignments(models.Model):
    classes = models.ForeignKey(classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_points=models.IntegerField(default=0)
    teacher_files = models.FileField(upload_to="assignments_given")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Assignments"


class Submit_Assignments(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Give_Assignments, on_delete=models.CASCADE)
    student_files = models.FileField(upload_to="assignments_submitted")
    obtain_points=models.IntegerField(default=0)

    def __str__(self):
        return self.student.first_name

    class Meta:

        verbose_name_plural = "Submissions"
