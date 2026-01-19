from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['Sr_no' ,'amount',  'date', 'description']
        labels = {
            'Sr_no ':'id',
            'amount': 'Expense Amount',
            'date': 'Date Received',
            'description': 'Notes',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date','description'] 