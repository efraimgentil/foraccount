from django.shortcuts import render
from expenses.models import Expense
from profits.models import Profit
from utils import UserUtil
# Create your views here.


def index(request):
    user =  UserUtil.get_current_user;
    resume = {
        "expenses":Expense.total_for(user)['value__sum'],
        "profits":Profit.total_for(user)["value__sum"]
    }
    
    return render( request , "main/index.html" , { "resume" : resume })
    
    