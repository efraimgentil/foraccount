from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
from forms import *
from django.contrib.auth.models import User
from models import ExpenseType
from main.utils import UserUtil

# Create your views here.


def index(request):
    form = ExpenseTypeSearchForm()
    expense_types = ExpenseType.objects.filter(user=UserUtil.get_current_user())
    return render(request , 'expense_types/index.html' , { "form" : form, "expense_types" : expense_types })

def search(request):
    form = ExpenseTypeSearchForm(request.GET or None)
    expense_types = ()
    if form.is_valid():
        expense_types = ExpenseType.objects.filter(name__icontains=form.cleaned_data['name'],
            user = UserUtil.get_current_user() )
    return render(request , "expense_types/index.html",
        { "form" : form , "expense_types" : expense_types })
    
def form(request):
    form = ExpenseTypeForm(request.POST or None)
    form.fields['father_expense_type'].queryset = ExpenseType.objects.filter( father_expense_type = None )
    if form.is_valid():
        expense_type = form.save(commit=False)
        expense_type.user = UserUtil.get_current_user()
        expense_type.save()
        return redirect("expense_types")
    return render(request , 'expense_types/form.html' , {"form" : form })

def edit(request , id):
    expense_type = ExpenseType.objects.get(pk=id  
        , user = UserUtil.get_current_user() )
    form = ExpenseTypeForm(request.POST or None , instance = expense_type )
    form.fields['father_expense_type'].queryset = ExpenseType.objects.filter( father_expense_type = None )
    if form.is_valid():
        form.save()
        return redirect("expense_types")
    return render(request , 'expense_types/form.html' , {"form" : form })
    
def delete(request , id):
    expense_type = ExpenseType.objects.get(pk=id  
        , user = UserUtil.get_current_user() )
    if request.POST:
        expense_type.delete()
        return redirect("expense_types")
    else:
        form = ExpenseTypeForm( instance=expense_type )
    return render(request , "expense_types/delete.html", { "form" : form })

def subtypes(request , id ):
    types = ExpenseType.objects.filter(father_expense_type=id,
        user = UserUtil.get_current_user() )
    data = []
    for i in types:
        data.append({ 
         "pk" : i.pk,
         "name" : i.name,
        })
    print( data )
    return JsonResponse(data , safe=False);