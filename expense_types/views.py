from django.shortcuts import render
from django.shortcuts import redirect
from forms import ExpenseTypeForm
from django.contrib.auth.models import User
from models import ExpenseType
from main.utils import CurrentUserUtil

# Create your views here.


def index(request):
    form = []
    expense_types = ExpenseType.objects.all()
    return render(request , 'expense_types/index.html' , { "form" : form, "expense_types"  : expense_types })
    
def form(request):
    form = ExpenseTypeForm(request.POST or None)
    if form.is_valid():
        expense_type = form.save(commit=False)
        expense_type.user = CurrentUserUtil.get_current_user()
        expense_type.save()
        return redirect("expense_types")
    return render(request , 'expense_types/form.html' , {"form" : form })

def edit(request , id):
    expense_type = ExpenseType.objects.get(pk=id  
        , user = CurrentUserUtil.get_current_user() )
    form = ExpenseTypeForm(request.POST or None , instance = expense_type )
    if form.is_valid():
        form.save()
        return redirect("expense_types")
    return render(request , 'expense_types/form.html' , {"form" : form })
    
def delete(request , id):
    expense_type = ExpenseType.objects.get(pk=id  
        , user = CurrentUserUtil.get_current_user() )
    if request.POST:
        expense_type.delete()
        return redirect("expense_types")
    else:
        form = ExpenseTypeForm( instance=expense_type )
    return render(request , "expense_types/delete.html", { "form" : form })
    