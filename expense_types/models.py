from django.db import models
from django.db.models import Sum, Case, When, DecimalField
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class ExpenseType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=True)
    user = models.ForeignKey(User)
    monthly = models.BooleanField(blank=True , null=False, default = False)
    
    def __str__(self):
      return self.name 
   
    
    @staticmethod 
    def month_resume(user, month = date.today().month ,  year = date.today().year ):
      return ExpenseType.objects.filter(user=user).values("name").annotate(
          sum_val = Sum(
              Case(
                  When(
                    expense__id__isnull=False,
                    expense__month=1,
                    expense__user= user,
                    then="expense__value",
                  ),
                  default=0,
                  output_field=DecimalField()
                  )
              )
          )
        
    