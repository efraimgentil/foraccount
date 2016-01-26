from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from main.utils import UserUtil
import datetime
# Create your models here.

class ProfitType(models.Model):
    
    name = models.CharField( blank=False , max_length=50)
    description = models.TextField(max_length=200, blank=True)
    monthly = models.BooleanField(default=False)
    user = models.ForeignKey(User , blank = False)
    
    def __str__(self):
        return "{}".format(self.name)

class Profit(models.Model):
    
    value = models.DecimalField( decimal_places = 2 , max_digits=20 , blank = False)
    date = models.DateField( blank = False )
    month = models.IntegerField( blank = False)
    year = models.IntegerField(blank = False)
    user = models.ForeignKey(User, blank = False ) 
    type = models.ForeignKey(ProfitType, blank= False,
     limit_choices_to={
        "user": UserUtil.get_current_user()
    })
    father_profit = models.ForeignKey('self', related_name="related_profits" , blank=True, null=True)
    
    def __str__(self):
        return "Profit[id={},value={},date={},month={},year={},user={}".format(self.id, self.value,
        self.date, self.month, self.year , self.user)
    
    @staticmethod
    def total_for(user, month = datetime.date.today().month , year= datetime.date.today().year):
        return Profit.objects.filter(user=user,month=month, year=year).aggregate(Sum("value"))
    


    
    