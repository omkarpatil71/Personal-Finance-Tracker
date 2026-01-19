from django.shortcuts import render, redirect,get_object_or_404
from .forms import ExpenseForm
from .models import Expense

def expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  
    else:
        form = ExpenseForm()
    return render(request, 'expense.html', {'form': form})

#expense_list display
def expense_list(request):
    expenses = Expense.objects.all()  # Get all expense entries
    return render(request, 'expense_list.html', {'expenses': expenses})

#delete entry
def delete_expense(request, Sr_no):
    expense = Expense.objects.get(Sr_no=Sr_no)
    expense.delete()
    return redirect('expense_list') 

#update entry
def update_expense(request, Sr_no):
    expense = get_object_or_404(Expense, Sr_no=Sr_no)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect to the expense list or any other page
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'update_expense.html', {'form': form})  