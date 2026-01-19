from django.db import models

# Create your models here.
# USer model

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    preferred_currency = models.CharField(max_length=10)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
