from django.db import models
from classes.models import classes

# Create your models here.
class EvaluationForm(models.Model):
    attendance_percentage = models.IntegerField()
    assignment_percentage = models.IntegerField()
    classes = models.ForeignKey(classes, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.classes.name - self.attendance_percentage - self.assignment_percentage
        )

    class meta:
        verbose_name_plural = "Evaluation Forms"
