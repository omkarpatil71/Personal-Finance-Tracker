from django.urls import path
from . import views
from .views import create_income,income_list,delete_income

urlpatterns = [
    path('create/', create_income, name='create_income'),
     path('list/', income_list, name='income_list'),
     path('list/create', create_income, name='create'),
 path('delete/<int:Sr_no>/', views.delete_income, name='delete_income'),
    path('update/<int:Sr_no>/', views.update_income, name='update_income'),
]
    # Add other URL patterns as needed
