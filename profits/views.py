from datetime import date
from django.shortcuts import render , redirect
from models import Profit , ProfitType
from main.utils import UserUtil
from forms import SearchProfitsForm , ProfitForm, SearchProfitTypesForm, ProfitTypeForm
# Create your views here.


def index(request):
    user = UserUtil.get_current_user()
    form = SearchProfitsForm()
    profits = Profit.objects.filter(user=user,  year = date.today().year , month = date.today().month )
    return render(request , "profits/index.html",
        { "profits" : profits, "form": form })
    
def search(request):
    user = UserUtil.get_current_user()
    form = SearchProfitsForm(request.GET or None)
    profits = []
    if form.is_valid():
        profits = Profit.objects.filter(user=user, year=form.data['year'], month=form.data['month'] )
    return render(request , "profits/index.html", { "form" : form , "profits" : profits})

def new(request):
    form = ProfitForm(request.POST or None)
    if form.is_valid():
        profit = form.save(commit=False)
        profit.user = UserUtil.get_current_user() 
        profit.month = profit.date.month
        profit.year = profit.date.year
        profit.save()
        return redirect("profits")
    
    return render(request , "profits/form.html" , { "form": form })

def edit(request , id ):
    form = ProfitForm( request.POST or None, instance = Profit.objects.get(pk=id, user=UserUtil.get_current_user() ) )
    if form.is_valid():
        profit = form.save(commit=False)
        profit.month = profit.date.month
        profit.year = profit.date.year
        profit.save()
        return redirect("profits")
    return render(request , "profits/form.html" , { "form": form } )
    
def delete(request, id ):
    if request.POST:
        profit = Profit.objects.get(pk=id , user=UserUtil.get_current_user() )
        profit.delete()
        return redirect("profits")
    else:
        form = ProfitForm(None ,instance = Profit.objects.get(pk=id , user=UserUtil.get_current_user() ))
    return render(request ,"profits/delete.html" , { "form" : form } )
    

def types_index(request):
    user = UserUtil.get_current_user()
    form = SearchProfitTypesForm()
    profit_types = ProfitType.objects.filter(user=user)
    return render(request , "profit_types/index.html" , {"form" : form , "profit_types" : profit_types  })
    
def types_new(request):
    form = ProfitTypeForm(request.POST or None)
    if form.is_valid():
        profit_type = form.save(commit=False)
        profit_type.user = UserUtil.get_current_user() 
        profit_type.save()
        return redirect("profit_types")
    
    return render(request , "profit_types/form.html" , { "form": form })
    
    user = UserUtil.get_current_user()
    form = SearchProfitTypesForm()
    
    return render(request , "profit_types/index.html" , {"form" : form })
    
    