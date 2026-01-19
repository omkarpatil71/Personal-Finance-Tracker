from django.shortcuts import render, redirect
from .forms import UserInfoForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user info to the database
            return redirect('base')  # Redirect to a success page or user list
    else:
        form = UserInfoForm()
    return render(request, 'register.html', {'form': form})


#login form
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')  # Adjust 'home' to your desired redirect
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})