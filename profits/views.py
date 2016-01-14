from django.shortcuts import render , redirect
from models import Profit
from main.utils import CurrentUserUtil
from forms import *
# Create your views here.


def index(request):
    user = CurrentUserUtil.get_current_user()
    form = SearchProfitsForm()
    profits = Profit.objects.filter(user=user,  year = date.today().year , month = date.today().month )
    return render(request , "profits/index.html",
        { "profits" : profits, "form": form })
    
def search(request):
    user = CurrentUserUtil.get_current_user()
    form = SearchProfitsForm(request.GET or None)
    profits = []
    if form.is_valid():
        profits = Profit.objects.filter(user=user, year=form.data['year'], month=form.data['month'] )
    return render(request , "profits/index.html", { "form" : form , "profits" : profits})