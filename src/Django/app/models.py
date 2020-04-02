from django.db import models
from django.utils import timezone
# Create your models here.

class UsersArray(models.Model):
    real_name        =  models.CharField(max_length=30)
    tz               = timezone.now()
    activity_periods = []

    
    # def __str__(self):              
    #     return self.real_name




