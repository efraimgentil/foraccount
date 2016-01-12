from django import forms
from .models import ExpenseType


class ExpenseTypeSearchForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs={"class":"form-control"}),
            max_length = 50,
            required=False)

class ExpenseTypeForm(forms.ModelForm):
    class Meta:
        model = ExpenseType
        fields = ['name' , 'description' ]
        widget = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "description" : forms.Textarea(attrs={"class" : "form-control"}),
        }
        