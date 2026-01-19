from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Budgets(models.Model):
    b_id=models.IntegerField(10)
    category=models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()

