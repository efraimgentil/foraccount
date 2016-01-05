from django.shortcuts import render
from django.shortcuts import redirect
from models import Expense
from forms import SearchExpensesForm
from forms import ExpenseForm
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
    form = ExpenseForm()
    if(request.POST):
        form = ExpenseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return  redirect( request , "expenses" )
        
    return render(request ,"expenses/form.html" , { "form" : form } ) 