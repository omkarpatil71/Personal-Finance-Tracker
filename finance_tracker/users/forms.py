from django import forms
from django.contrib.auth.forms import  AuthenticationForm
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['Name', 'Last_name', 'Email', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Use a password input field for security
        }

        labels = {
            'Name': 'First Name',
            'Last_name': 'Last Name',
            'Email': 'Email Address',
            'password': 'Password',
        }

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if UserInfo.objects.filter(Email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserInfo
        fields = ['Email', 'password']

        labels = {
            'Email': 'Email Address',
            'password': 'Password',
        }