from django.shortcuts import render, redirect,get_object_or_404 
from django.contrib import messages
from .forms import IncomeForm
from .models import Income

from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm  # Make sure you have a form set up for Income

def create_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income_list')  
    else:
        form = IncomeForm()
    return render(request, 'income.html', {'form': form})

def income_list(request):
    incomes = Income.objects.all()  # Get all income entries
    return render(request, 'income_list.html', {'incomes': incomes}) 



def delete_income(request, Sr_no):
    income = get_object_or_404(Income, Sr_no=Sr_no)
    income.delete()
    return redirect('income_list')



def update_income(request, Sr_no):
    income = get_object_or_404(Income, Sr_no=Sr_no)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'update_income.html', {'form': form})
