from django.shortcuts import render,redirect
from .forms import BudgetsForm
from .models import Budgets

# Create your views here.
def budgets(request):
    if request.method == 'POST':
        form = BudgetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget')  
    else:
        form = BudgetsForm()
    return render(request, 'budget.html', {'form': form})