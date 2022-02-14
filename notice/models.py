from django.db import models
from classes.models import classes
from customuser.models import User
# Create your models here.
class notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files=models.FileField(upload_to='notice/files/',blank=True)
    publish_to=models.ForeignKey(classes,on_delete=models.CASCADE)
    publish_by=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = "Notices"


class global_notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files=models.FileField(upload_to='notice/files/',blank=True)
    publish_to=models.ForeignKey(User,on_delete=models.CASCADE)
    publish_by=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = "Global Notices"





    

