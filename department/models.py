from django.db import models
from customuser.models import User

# Create your models here.
class department(models.Model):
    name = models.CharField(null=True, unique=True, max_length=100)
    description = models.TextField(null=True)
    alias = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Departments"


class Departmentadmin_info(models.Model):
    dept_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department}"

    class Meta:
        verbose_name_plural = "Departmentadmin_info"
