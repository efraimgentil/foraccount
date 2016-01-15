from django import forms
from main.utils import DateUtil
from datetime import date
from models import Profit

class SearchProfitsForm(forms.Form):
    
    year = forms.ChoiceField(required=True,
        widget=forms.Select(attrs={"class":"form-control"}),
        choices=((str(x),x) for x in DateUtil.YEARS),
        initial = date.today().year )
    month = forms.ChoiceField(required=True,
        widget=forms.Select(attrs={"class":"form-control"}),
        choices =((str(x) , x) for x in DateUtil.MONTHS),
        initial = date.today().month)
        

class ProfitForm(forms.ModelForm):
    
    class Meta:
        model = Profit
        fields = ['value' , 'date'] 
        widgets = {
            "value" : forms.NumberInput(attrs={"class":"form-control"}),
            "date" : forms.DateInput(attrs={"class":"form-control"})
        }
    