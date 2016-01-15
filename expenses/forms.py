from django import forms
from datetime import date
from main.utils import DateUtil
from models import Expense
from expense_types.models import ExpenseType
from main.utils import UserUtil


class SearchExpensesForm(forms.Form):
    
    year = forms.ChoiceField(required=True , 
        widget=forms.Select(attrs={"class":"form-control"}),
        choices =  ((str(x), x) for x in DateUtil.YEARS ) , initial = date.today().year )
    month = forms.ChoiceField(required=True ,
        widget=forms.Select(attrs={"class":"form-control"}),
        choices = ((str(x), x) for x in DateUtil.MONTHS ) , initial = date.today().month )
    
    def is_valid(self):
        valid = True
        if not super(SearchExpensesForm , self).is_valid():
            valid = False
        return valid

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = [ 'value' , 'date_expense' , 'type'  ]
        expense_types = ExpenseType.objects.filter(user=UserUtil.get_current_user())
        widgets = {
            'year': forms.Select(choices = ((str(x), x) for x in DateUtil.YEARS ), attrs={'class': 'form-control'}),
            'month': forms.Select(choices = ((str(x), x) for x in DateUtil.MONTHS ) , attrs={'class': 'form-control'} ),
            'date_expense' : forms.DateInput(attrs={"class" :"form-control" } ),
            'value' : forms.NumberInput(attrs={"class" :"form-control" , "s" :"lol"} ),
        }
    