from django.shortcuts import render
from expenses.models import Expense
from profits.models import Profit
from expense_types.models import ExpenseType
from utils import UserUtil , DateUtil
from datetime import date
# Create your views here.


def index(request):
    month = int( request.GET.get("month") or date.today().month )
    year  = int( request.GET.get("year") or date.today().year )
    
    user =  UserUtil.get_current_user;
    resume = {
        "expenses": Expense.total_for(user,month,year)['value__sum'] or 0.0,
        "profits" : Profit.total_for(user,month,year)["value__sum"] or 0.0
    }
    
    month_expenses = ExpenseType.month_resume( user=user, month=month, year=year );
    
    return render( request , "main/index.html" ,
        {
          "resume" : resume,
          "month_expenses": month_expenses,
          "years" : DateUtil.YEARS,
          "months" : DateUtil.MONTHS,
          "selected_month" : month, 
          "selected_year" : year,
        })
    
    