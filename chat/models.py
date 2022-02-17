from django.db import models
from customuser.models import User


class Messages(models.Model):

    sender = models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver",on_delete=models.CASCADE)
    msg = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Messages"
    
    def __str__(self):
        return str(self.id) + ": from " + str(self.sender) + " to " + str(self.receiver)