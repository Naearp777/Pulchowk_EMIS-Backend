from django.db import models

from classes.models import classes
# Create your models here.



class materials(models.Model):
    material_name=models.CharField(null=True, max_length=100)
    classes=models.ForeignKey(classes,on_delete=models.CASCADE)
    upload=models.FileField(upload_to="materials",default='avatar.jpg')

    def __str__(self):
        return f'{self.material_name}'

    class Meta:
        verbose_name_plural = "material_name"