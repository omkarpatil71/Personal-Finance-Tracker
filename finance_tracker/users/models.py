from django.db import models

#user registration
class UserInfo(models.Model):
    Name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)  
    password = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.Name} {self.Last_name}"
