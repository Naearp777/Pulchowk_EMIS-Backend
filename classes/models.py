from django.db import models
from customuser.models import User
# Create your models here.
class classes(models.Model):
    class_name=models.CharField(null=True, unique=True, max_length=100)
    teacher=models.ManyToManyField(User,related_name='teacher')
    student=models.ManyToManyField(User)

    def __str__(self):
        return f'{self.class_name}'

    class Meta:
        verbose_name_plural = "Class"