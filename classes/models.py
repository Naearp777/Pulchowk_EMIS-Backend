from django.db import models
from customuser.models import User
from department.models import department
from batch.models import batch
from section.models import section

# Create your models here.
class classes(models.Model):
    name = models.CharField(null=True, max_length=100)
    alias = models.CharField(null=True, max_length=100)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(section, on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField(User, related_name="teacher")
    student = models.ManyToManyField(User)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Class"
