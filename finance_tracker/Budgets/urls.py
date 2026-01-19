from django.urls import path
from . import views
from .views import budgets

urlpatterns=[

path('budget/', budgets, name='budgets'),

]
