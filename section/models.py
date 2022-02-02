from django.db import models
from batch.models import batch
from department.models import department
# Create your models here.
class section(models.Model):
    
    section=models.CharField(null=True, unique=True, max_length=100)
    def __str__(self):
        return f'{self.section}'

    class Meta:
        verbose_name_plural = "Section"