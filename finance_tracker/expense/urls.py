from django.urls import path
from . import views
from .views import expense,expense_list

urlpatterns = [
    path('expense/', expense, name='expense'),
     path('expense_list/', expense_list, name='expense_list'),
     path('expense_list/expense', expense, name='expense'),
     path('delete_expense/<int:Sr_no>/', views.delete_expense, name='delete_expense'),
     path('update_expense/<int:Sr_no>/', views.update_expense, name='update_expense'),
    # Add other URL patterns as needed
]