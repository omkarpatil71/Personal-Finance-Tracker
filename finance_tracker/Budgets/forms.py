from django import forms
from .models import Budgets

class BudgetsForm(forms.ModelForm):
    class Meta:
        model = Budgets
        fields = ['b_id' ,'category',  'amount', 'date']
        labels = {
            'b_id ':'id',
            'category':'Category',
            'amount': 'Amount',
            'date': 'Date Received',
            
        }