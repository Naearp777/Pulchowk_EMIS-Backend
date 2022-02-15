from django.db import models
from customuser.models import User
# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_to = models.ForeignKey(User,on_delete=models.CASCADE)
    publish_by = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notifications"
