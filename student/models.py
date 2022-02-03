from django.db import models
from batch.models import batch
from department.models import department
from section.models import section
from customuser.models import User
# Create your models here.
class student_info(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.ForeignKey(department ,on_delete=models.CASCADE)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    section=models.ForeignKey(section,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.student}--{self.section}--{self.batch}--{self.department}'

    class Meta:
        verbose_name_plural = "student_info"
