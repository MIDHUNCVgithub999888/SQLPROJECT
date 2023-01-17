from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Registration(models.Model):
    desk=RegexValidator(regex=r'^[0-9]{5}$',message="Enter the correct 9 digits")
    Date=models.DateField(auto_now_add=False, auto_now=False,null=True)
    CustomerName=models.CharField(max_length=100)
    AnyDeskId=models.IntegerField()
    ApplicationDetails=models.CharField(max_length=100)
    Requirements=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    CompletionDate=models.DateField(auto_now_add=False, auto_now=False,null=True)
    staff =models.CharField(max_length=100)

class StaffTb(models.Model):
    Registration=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=100)
    DateOfBirth=models.DateField(auto_now_add=False,null=True)
    Address=models.CharField(max_length=100,default='')






