from django import forms
from main.utils import DateUtil
from datetime import date
from models import Profit , ProfitType
from main.utils import UserUtil

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
        fields = ['type' , 'value' , 'date'] 
        widgets = {
            "value" : forms.NumberInput(attrs={"class":"form-control"}),
            "date" : forms.DateInput(attrs={"class":"form-control"})
        }
    

class SearchProfitTypesForm(forms.Form):
    
    name = forms.CharField(required=False,
            widget = forms.TextInput(attrs={"class":"form-control"}),
            max_length=50)
    monthly = forms.BooleanField(required=False)
    

class ProfitTypeForm(forms.ModelForm):
    
    class Meta:
        model = ProfitType
        fields = [ 'name' , 'description' , 'monthly']