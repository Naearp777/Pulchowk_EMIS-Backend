from django.db import models

from batch.models import Batch
from datetime import datetime  , timedelta
# Create your models here.
class Semester(models.Model):
    sem_name = models.CharField(max_length=15)
    year = models.PositiveSmallIntegerField()
    part = models.CharField(max_length=10)
    # batch = models.ForeignKey(Batch, on_delete=models.CASCADE) # This introducing errors.
    sem_start_date = models.DateField(auto_now = False)
    sem_end_date = models.DateField(auto_now=False)