from django import forms
from main.utils import DateUtil
from datetime import date

class SearchProfitsForm(forms.Form):
    
    year = forms.ChoiceField(required=True,
        widget=forms.Select(attrs={"class":"form-control"}),
        choices=((str(x),x) for x in DateUtil.YEARS),
        initial = date.today().year )
    month = forms.ChoiceField(required=True,
        widget=forms.Select(attrs={"class":"form-control"}),
        choices =((str(x) , x) for x in DateUtil.MONTHS),
        initial = date.today().month)
    