from django.shortcuts import render
from models import Expense
from forms import SearchExpensesForm
from forms import ExpenseForm
from forms import ExpenseModelForm
# Create your views here.


def index(request):
    form = SearchExpensesForm()
    return render(request ,"expenses/index.html" , { "expenses": [] , "form" : form  }) 

def search(request):
    form = SearchExpensesForm(request.GET)
    expenses = []
    if( form.is_valid ):
        expenses = Expense.objects.filter(year = form.data['year'] , month = form.data['month'])
    
    return render(request ,"expenses/index.html" , { "expenses": expenses , "form" : form }) 
    

def new(request):
    form = ExpenseModelForm()
    return render(request ,"expenses/form.html" , { "form" : form } ) 