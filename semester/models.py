from django.db import models
from batch.models import Batch
# Create your models here.
class Semester(models.Model):
    sem_name = models.CharField(max_length=15)
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    # What are other attributes that we need to add?
    sem_start_date = models.DateField()
    sem_end_date = models.DateField()
    
    # def __str__(self):
    #     return self.batch.batch_name    
    # def __str__(self):
    #     return self.sem_name