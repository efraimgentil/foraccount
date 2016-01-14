from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profit(models.Model):
    
    value = models.DecimalField( decimal_places = 2 , max_digits=20 , blank = False)
    date = models.DateField( blank = False )
    month = models.IntegerField( blank = False)
    year = models.IntegerField(blank = False)
    user = models.ForeignKey(User, blank = False ) 
    
    def __str__(self):
        return "Profit[value={},date={},month={},year={},user={}".format(self.value,
        self.date, self.month,self.year , self.user)
    