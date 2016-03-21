from datetime import date
from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        messages.success(request, "Record created with success" )
        return HttpResponseRedirect( "{}?month={}&year={}".format( reverse("search_profits"), profit.month , profit.year))
    return render(request , "profits/form.html" , { "form": form })

def edit(request , id ):
    form = ProfitForm( request.POST or None, instance = Profit.objects.get(pk=id, user=UserUtil.get_current_user() ) )
    if form.is_valid():
        profit = form.save(commit=False)
        profit.month = profit.date.month
        profit.year = profit.date.year
        profit.save()
        messages.success(request, "Record updated with success" )
        return HttpResponseRedirect( "{}?month={}&year={}".format( reverse("search_profits") , profit.month , profit.year ))
    return render(request , "profits/form.html" , { "form": form } )
    
def delete(request, id ):
    profit = Profit.objects.get(pk=id , user=UserUtil.get_current_user() )
    if request.POST:
        profit.delete()
        messages.success(request, "Record deleted with success" )
        return HttpResponseRedirect( "{}?month={}&year={}".format( reverse("search_profits") , profit.month , profit.year) )
    form = ProfitForm(None ,instance = profit)
    return render(request ,"profits/delete.html" , { "form" : form } )
    

def types_index(request):
    user = UserUtil.get_current_user()
    form = SearchProfitTypesForm()
    profit_types = ProfitType.objects.filter(user=user)
    return render(request , "profit_types/index.html" ,
        {"form" : form ,
         "profit_types" : profit_types})
    
def types_new(request):
    form = ProfitTypeForm(request.POST or None)
    if form.is_valid():
        profit_type = form.save(commit=False)
        profit_type.user = UserUtil.get_current_user() 
        profit_type.save()
        messages.success(request, "Record created with success" )
        return redirect("profit_types")
    
    return render(request , "profit_types/form.html" , { "form": form })
    
    
def types_edit(request , id):
    instance = ProfitType.objects.get(pk=id , user = UserUtil.get_current_user())
    form = ProfitTypeForm( request.POST or None , instance=instance)
    if form.is_valid():
        profit_type = form.save(commit=False)
        profit_type.save()
        messages.success(request, "Record updated with success" )
        return redirect("profit_types")
    
    return render(request , "profit_types/form.html", {"form" : form })
        
def types_delete(request , id):
    instance = ProfitType.objects.get(pk=id , user = UserUtil.get_current_user())
    if request.POST:
        instance.delete()
        messages.success(request, "Record deleted with success" )
        return redirect("profit_types")
    form = ProfitTypeForm(  instance=instance)
    return render(request , "profit_types/delete.html", {"form" : form })
        
        