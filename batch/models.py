from django.db import models
from department.models import department

# Create your models here.
class batch(models.Model):
    name = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Batch"
