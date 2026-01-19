from django.db import models
from django.contrib.auth.models import User

#expense module
class Expense(models.Model):
    Sr_no = models.IntegerField(primary_key=True, ) 
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"  {self.description} - {self.amount}"