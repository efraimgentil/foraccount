from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExpenseType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User)
    
    def __str__(self):
      return self.name 
   
    