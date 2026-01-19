from django.db import models
from django.contrib.auth.models import User

#income module
class Income(models.Model):
    Sr_no = models.IntegerField(primary_key=True, )  # Primary key, manually assigned
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f" {self.source} - {self.amount}"
