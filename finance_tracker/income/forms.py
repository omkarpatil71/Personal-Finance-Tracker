from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['Sr_no' ,'amount', 'source', 'date', 'description']
        labels = {
            'Sr_no ':'id',
            'amount': 'Income Amount',
            'source': 'Income Source',
            'date': 'Date Received',
            'description': 'Notes',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }



class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date'] 