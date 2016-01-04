from django.db import models

# Create your models here.


class Expense(models.Model):
    year         = models.IntegerField( blank = False )
    month        = models.IntegerField( blank = False )
    date_expense = models.DateField( blank = False )
    value        = models.DecimalField(max_digits = 20, decimal_places = 2, blank = False )
    
    
    