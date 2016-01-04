from django import forms
from datetime import date
from models import Expense
from main.utils import Date


class SearchExpensesForm(forms.Form):
    
    YEARS = ((str(x), x) for x in range(2013 , date.today().year + 1 ))
    MONTHS = ((str(x), x) for x in range( 1 , 13  ))
    
    year = forms.ChoiceField(required=True ,  widget=forms.Select(attrs={"class":"form-control"}), choices = YEARS  )
    month = forms.ChoiceField(required=True ,  widget=forms.Select(attrs={"class":"form-control"}) , choices = MONTHS )
    
     
    def is_valid(self):
        valid = True
        if not super(SearchExpensesForm , self).is_valid():
            valid = False
        return valid

class ExpenseForm(forms.Form):
    
    YEARS = ((str(x), x) for x in range(2013 , date.today().year + 1 ))
    MONTHS = ((str(x), x) for x in range( 1 , 13  ))
    
    year = forms.ChoiceField(required=True, widget=forms.Select(attrs={"class":"form-control"}), choices = YEARS)
    month = forms.ChoiceField(required=True , widget=forms.Select(attrs={"class":"form-control"}), choices = MONTHS)
    date = forms.DateField(required = True , widget=forms.DateInput(attrs={"class":"form-control"}) )
    value = forms.DecimalField(required=True, decimal_places=2 , widget=forms.NumberInput(attrs={"class":"form-control"}) )
    
    
    def is_valid(self):
        
        return True

class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['year' , 'month' , 'date_expense' , 'value']
        widgets = {
            'year': forms.Select(attrs={'class': 'form-control'} , choices = Date.years_available()  ),
            'month': forms.Select(attrs={'class': 'form-control'} , choices = Date.months_available() ),
        }
    