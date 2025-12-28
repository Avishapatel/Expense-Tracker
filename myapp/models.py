from django.db import models
from .models import *

# Create your models here.
class Category(models.Model):
    cat_name=models.TextField(max_length=10)
    def __str__(self):
        return self.cat_name

class Register(models.Model):
    full_name=models.CharField(max_length=100)
    salary = models.IntegerField(null=True, blank=True)
    email_id=models.EmailField()
    phone_no=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
    
class Add_Expense(models.Model):
    register_user=models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    title=models.TextField()
    amount=models.FloatField()
    category=models.TextField()
    def __str__(self):
        return self.title + '-' +str(self.amount) + '-' +self.category
    

