from django.db import models
from department.models import department
# Create your models here.
class Teachers_info(models.Model):
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.department}'
    
    class Meta:
        verbose_name_plural = "Teachers_info"