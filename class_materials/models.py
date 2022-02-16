from django.db import models
from customuser.models import User
from classes.models import classes

# Create your models here.


class folder(models.Model):
    classes = models.ForeignKey(classes, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.folder_name

    class Meta:
        verbose_name_plural = "folder"


class materials(models.Model):
    folder = models.ForeignKey(folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to="materials/", default="avatar.jpg")
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name_plural = "materials"
