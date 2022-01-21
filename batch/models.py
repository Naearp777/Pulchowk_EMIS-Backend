from django.db import models

# Create your models here.
class Batch(models.Model):
    # batch_ID = models.CharField(max_length=10)
    batch_YR = models.CharField(max_length=10)
