from django.db import models
from batch.models import batch
from department.models import department
# Create your models here.
class section(models.Model):
    department=models.ForeignKey(department ,on_delete=models.CASCADE)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    section=models.CharField(null=True, unique=True, max_length=100)
    def __str__(self):
        return f'{self.section}--{self.batch}--{self.department}'

    class Meta:
        verbose_name_plural = "Section"