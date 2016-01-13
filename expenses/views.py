from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from datetime import date
from models import Expense
from forms import SearchExpensesForm
from forms import ExpenseForm
from main.utils import CurrentUserUtil
# Create your views here.


def index(request):
    form = SearchExpensesForm()
    expenses = Expense.objects.filter(year = date.today().year , month = date.today().month )
    return render(request ,"expenses/index.html" , { "expenses": expenses, "form" : form  }) 

def search(request):
    form = SearchExpensesForm(request.GET )
    expenses = []
    if( form.is_valid ):
        expenses = Expense.objects.filter(year = form.data['year'] , month = form.data['month'])
    
    return render(request ,"expenses/index.html" , { "expenses": expenses , "form" : form }) 
    

def new(request):
    form = ExpenseForm(initial = { 'year' : date.today().year , 'month' : date.today().month })
    if(request.POST):
        form = ExpenseForm(request.POST)
        if(form.is_valid()):
            expense = form.save(commit=False)
            expense.user = CurrentUserUtil.get_current_user()
            expense.year = expense.date_expense.year
            expense.month = expense.date_expense.month
            expense.save()
            return  redirect( "expenses" )
        
    return render(request ,"expenses/form.html" , { "form" : form } ) 
    
def edit(request , id):    
    if(request.POST):
        form = ExpenseForm(request.POST, instance = Expense.objects.get(pk=id))
        if form.is_valid():
            expense = form.save(commit=False)
            expense.year = expense.date_expense.year
            expense.month = expense.date_expense.month
            form.save()
            return redirect("expenses")
    else:
        form = ExpenseForm(instance = Expense.objects.get(pk=id))
    return render(request ,"expenses/form.html" , { "form" : form } ) 
    
def delete(request , id):  
    if(request.POST):
        expense = Expense.objects.get(pk=id)
        expense.delete()
        return redirect("expenses")
    else:
        form = ExpenseForm(instance = Expense.objects.get(pk=id))
    return render(request ,"expenses/delete.html" , { "form" : form  } ) 