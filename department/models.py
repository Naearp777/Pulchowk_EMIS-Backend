from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(null=True, unique=True, max_length=100)
    description=models.TextField(null=True)
    def __str__(self):
        return f'{self.department_name}'

    class Meta:
        verbose_name_plural = "Departments"
