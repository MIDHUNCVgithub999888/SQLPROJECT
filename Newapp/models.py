from importlib._common import _
from django.db import models
from django.core.validators import RegexValidator
import  datetime

# Create your models here.

class Registration(models.Model):
    desk=RegexValidator(regex=r'^[0-9]{5}$',message="Enter the correct 9 digits")
    Date=models.DateField(default=datetime.date.today)
    CustomerName=models.CharField(max_length=100)
    AnyDeskId=models.IntegerField()
    ApplicationDetails=models.CharField(max_length=100)
    Requirements=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    CompletionDate=models.DateField(auto_now_add=False, auto_now=False,null=True)
    Staff =models.CharField(max_length=100)


class StaffTb(models.Model):
    Registration=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=100)
    DateOfBirth=models.DateField(auto_now_add=False,null=True)
    Address=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.Name






