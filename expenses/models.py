from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from expense_types.models import ExpenseType
from main.utils import UserUtil
from datetime import date

# Create your models here.


class Expense(models.Model):
    year         = models.IntegerField( blank = False )
    month        = models.IntegerField( blank = False )
    date_expense = models.DateField( blank = False )
    value        = models.DecimalField(max_digits = 20, decimal_places = 2, blank = False )
    description  = models.TextField( blank = True, null=True, max_length = 200 )
    type         = models.ForeignKey( ExpenseType 
        , blank = False
        , related_name="expense"
        , limit_choices_to={
            'user' : UserUtil.get_current_user(),
            'father_expense_type' : None
        })
    subtype      = models.ForeignKey( ExpenseType
        , null = False
        , related_name="expense_subtypes")
    user         = models.ForeignKey(User)
    
    @staticmethod
    def total_for(user, month=date.today().month  , year=date.today().year  ):
        return Expense.objects.filter(user=user,year=year,month=month).aggregate(Sum("value"))
       
